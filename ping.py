import sys
import subprocess 

my_device = sys.argv[1]

if __name__ == '__main__':
    try:
      pingping = subprocess.Popen(["ping", my_device],stdout=subprocess.PIPE)
      
      while True:
        line = pingping.stdout.readline()
        if not line:
          break

        connected_device = line.decode('utf-8').split()[3]
        
        if my_device in connected_device:
          print(connected_device)
          subprocess.Popen(["write", "connected to network"])
    
    except KeyboardInterrupt:
        print(sys.stderr, '\nExiting by user request.\n')
        sys.exit(0)
