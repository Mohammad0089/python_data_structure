from collections import ChainMap

import argparse
import os

car_parts = {'hood': 500, 'engine': 5000, 'front_door': 750}
car_options = {'A/C': 1000, 'Turbo': 2500, 'rollbar': 300}
car_accessories = {'cover': 100, 'hood_ornament': 150, 'seat_cover': 99}
car_pricing = ChainMap(car_accessories, car_options, car_parts)

#print(car_pricing)
#print(car_pricing['hood'])

# in this we will do a showcase how chainMap can be used in app;ication
# lets say our app gets some values from commandline 
# also, some values from OS 
# and finally there is app default values
#
# piorioty is in the following order: commandline, OS values, app default
# so first we check for the value in that following order 
# we can acheive this strategy by using chainMap.
def main():
    # lets define application default values
    app_defualt={'username':'admin',
                 'password': 'admin'}
    
    # lets define commandline arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-u','--username')
    parser.add_argument('-p','--password')
    
    # now we need to convert commandline args to dict method_1
        # args here is list[tuples]
        
    # args = parser.parse_args()._get_kwargs()
    # command_line_arguments = {key:value for key, value in args if value}
    
    # now we need to convert commandline args to dict method_2
    args = parser.parse_args()
    command_line_arguments = {key:value for key, value in vars(args).items() if value}
    
# The other cool piece here is the use of Python’s built-in vars.
# If you were to call it without an argument, vars would behave like Python’s built-in locals.
# But if you do pass in an object, then vars is the equivalent to object’s __dict__ property.
# In other words, vars(args) equals args.__dict__.
    
    
    chain = ChainMap(command_line_arguments, os.environ, app_defualt)
    
    print(chain.get('username'))
    
if __name__=='__main__':
    main()
    os.environ['username'] = "test"
    main()