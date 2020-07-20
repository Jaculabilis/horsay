#!/usr/bin/env python3


from argparse import ArgumentParser
from sys import stdin, stdout


def parse_args():
	parser = ArgumentParser(description="Displays input straight from the horse's mouth.")
	parser.add_argument("-u", "--unicode", action="store_true",
		help="Use fancier lines for the text bubble")
	parser.add_argument("-w", "--max-width", type=int, default=80,
		help="Maximum width of output (default: 80)")
	parser.add_argument("-b", "--break-at", type=str, default=" -",
		help="String of characters to break words at (default: space and -)")
	return parser.parse_args()


def segment_line(line, max_width, break_at):
	"""
	Breaks a line of text into multiple lines on word boundaries where possible.
	"""
	# The horse and text box take up 19 characters' worth of space
	limit = max_width - 19
	segments = []
	while len(line) > limit:
		# Find the first breakable character.
		# Assume we'll find one for simplicity.
		i = limit
		while limit > 0 and line[i] not in break_at:
			i -= 1
		# Break off a segment
		segments.append(line[:i])
		line = line[i:].lstrip()
	# Include the remainder once the line is short enough
	segments.append(line)
	return segments


def get_bubble_chars(use_unicode):
	"""
	Gets the characters to use for the text bubble.
	"""
	if use_unicode:
		tl_corner = "\u256D"
		tr_corner = "\u256E"
		bl_corner = "\u2570"
		br_corner = "\u256F"
		horizontal = "\u2500"
		vertical = "\u2502"
		tail = "\u2524"
	else:
		tl_corner = "+"
		tr_corner = "+"
		bl_corner = "+"
		br_corner = "+"
		horizontal = "-"
		vertical = "|"
		tail = "|"
	return tl_corner, tr_corner, bl_corner, br_corner, horizontal, vertical, tail


def build_bubble_lines(segments, bubble_chars):
	"""
	Builds a text bubble containing the given text segments.
	"""
	tl, tr, bl, br, horiz, vert, tail = bubble_chars
	max_width = max(map(len, segments))
	prefix = "{}{}{}{}{}".format(tl, horiz, horiz * max_width, horiz, tr)
	suffix = "{}{}{}{}{}".format(bl, horiz, horiz * max_width, horiz, br)
	mid = ["{0} {1:{2}} {0}".format(vert, seg, max_width) for seg in segments]
	return [prefix, *mid, suffix]


def build_horse_lines(bubble_chars):
	"""
	Returns the lines making up the horse.
	"""
	_, _, _, _, horiz, _, _ = bubble_chars
	return [
		"     ./|,,/|   ",
		"    <   o o)   ",
		"   <\ (    | {0}{0}".format(horiz),
		"  <\\\  |\  |   ",
		" <\\\\\  |(__)   ",
		"<\\\\\\\  |       "
	]


def combine_lines(horse, bubble, bubble_chars):
	"""
	Aligns the text bubble with the horse based on the bubble's size.
	"""
	_, _, _, _, horiz, _, tail = bubble_chars
	# Align the horse and text bubble
	if len(bubble) < 4:
		bubble = [""] + bubble
	if len(bubble) > len(horse):
		horse = [" " * len(horse[0])] * (len(bubble) - len(horse)) + horse
	elif len(bubble) < len(horse):
		bubble = bubble + [""] * (len(horse) - len(bubble))
	combined = []
	for h, b in zip(horse, bubble):
		if h[-1] == horiz:
			b = tail + b[1:]
		combined.append(h + b)
	return combined


def main():
	args = parse_args()
	segments = segment_line(stdin.readline().strip(), args.max_width, args.break_at)
	chars = get_bubble_chars(args.unicode)
	text_half = build_bubble_lines(segments, chars)
	horse_half = build_horse_lines(chars)
	combined = combine_lines(horse_half, text_half, chars)
	for line in combined:
		stdout.write(line + "\n")

if __name__ == "__main__":
	main()
