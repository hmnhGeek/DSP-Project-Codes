import argparse as ap
import pvd

parser = ap.ArgumentParser()
parser.add_argument('image', type=str, help="Image location")
parser.add_argument('blocks', type=int, help="Number of blocks.")
args = parser.parse_args()

if args.image and args.blocks:
    angles = pvd.step1(args.image, args.blocks)
