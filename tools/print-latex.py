import argparse
import matplotlib.pyplot as plt

# Set args
parser = argparse.ArgumentParser(description='Print out the latex.')
parser.add_argument('latex_str', type=str, nargs=1,
                   help='the latex string')
parser.add_argument('--file', type=str, nargs=1,
                   help='save to file name.')

# Get latex string
args = parser.parse_args()

print(args)
latex_str = args.latex_str[0]

# Create Plot
ax = plt.axes([0,0,0.3,0.3]) #left,bottom,width,height
ax.set_xticks([])
ax.set_yticks([])
ax.axis('off')
plt.text(0.2,0.2,'$%s$' %latex_str,size=50)

if args.file is not None and len(args.file)>0:
    filename_to_save = args.file[0]
    plt.savefig(filename_to_save)
else:
    plt.show()
