import os
import shutil
from sklearn.model_selection import train_test_split
import argparse


def split_data(src, dst_train, dst_test, pct_test):
    # Get list of all files in source directory
    src_file_paths = [src + '/' + file for file in os.listdir(src)]

    # Split list of files into train and test sets
    train, test = train_test_split(src_file_paths, test_size=pct_test, random_state=1)

    # Copy train files to destination directory
    for file in train:
        shutil.copy(file, dst_train)
    
    # Copy test files to destination directory
    for file in test:
        shutil.copy(file, dst_test)
    

def main(args):
    # Check for valid percentage
    if args.pct_train <= 0 or args.pct_train >= 1.0:
        raise Exception('Invalid value for percentage train argument. Please enter a float value between 0.0 and 1.0!')
    
    # Obtain percentage test
    pct_test = 1.0 - args.pct_train

    # Spplit the data into train and test
    split_data(args.source, args.dest_train, args.dest_test, pct_test)
    
    print("Data splitting completed successfully!")


if __name__=='__main__':
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        prog="Script for splitting dataset into train and test sets",
        epilog="Example usage: split_dataset.py --source ./time-of-day-dataset/daytime --dest-train ./train_dataset/daytime --dest-test ./test_dataset/daytime --pct-train 0.8"
    )
    parser.add_argument("--source", default="", help="Path to source directory containing data for splitting.")
    parser.add_argument("--dest-train", default="", help="Path to destination directory for saving train data.")
    parser.add_argument("--dest-test", default="", help="Path to destination directory for saving train data.")
    parser.add_argument("--pct-train", type=float, default=0.8, help="Percentage of data to be allocated to train set. The remaining data will be allocated to test set. Defaults to 0.8, i.e. 80% train and 20% test.")
    args = parser.parse_args()

    print("Command Line Args: ", args)

    # Pass command line arguments to main function
    main(args)