import argparse

def get_args():
    parser = argparse.ArgumentParser(
        description="A simple arguments parser",
        epilog="This is where you  might put example usage"
    )

    # required argument
    parser.add_argument("-x", action="store", required=True, help= "help guide for x flag")
    
    #optional arguments
    parser.add_argument('-y', help= "help guide for y flag", default=False)
    parser.add_argument('-z', help= "helpguide for z flag", type=int, required=False)
    
    
    print(parser.parse_args())


if __name__ == '__main__':
    get_args()