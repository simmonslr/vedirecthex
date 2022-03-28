##################################
# Created on Mar 13, 2022
# @author: lsimmons
##################################
import sys, getopt, serial

ver = "v1.2 03/24/2022"

####################################
#                                  #
####################################
def main ( argv ):
    port = ''
    cmd  = ""

    try:
        opts, args = getopt.getopt ( argv,"hp:c:", ["port=","cmd="] )
    except getopt.GetoptError:
        print ( "vedirecthex.py -p <port> -c <cmd>" )
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print ( 'vedirecthex.py -p <port> -c <cmd>' )
            sys.exit()
        elif opt in ("-p", "--port"):
            port = arg
        elif opt in ("-c", "--cmd"):
            cmd = arg

    print ( "===========")
    print ( "vedirecthex")
    print ( ver )
    print ( "port: " + port )
    ser = serial.Serial ( port, 19200, timeout=10 )
    ser.close()

    ser.open()
    ser.write ( str.encode ( ":451\n" ))        # get product ID
    read_val = ser.read ( size = 16 )
    print ( "prod: " +bytes.decode ( read_val ))
    ser.close()
    
    ser.open()
    print ( " cmd: " + cmd )
    ser.write ( str.encode ( cmd + "\n" ))
    read_val = ser.read ( size = 256 )
    print ( " res: " + bytes.decode ( read_val ))
    ser.close()

####################################
#                                  #
####################################
if __name__ == '__main__':
    pass
    main ( sys.argv[1:] )
