import os
import shutil

from datetime import datetime
"""Total five logs files are available. Each log file content has timestamp data.
   step 1: Rename file with timestamp
   """
def main():
    directory_list = []
    kiwi_values_list = []
    
    
    def renameDir(dire):
        with open (dire + "/fruit.log") as log:
            timestamp = datetime.strptime(log.readline(15), "%b %d %H:%M:%S")
        shutil.move(dire,str(timestamp))
        directory_list.append(str(timestamp))

    #Stored value of Kiwi in list
    def kiwi_values(kiwi_string):
        try:
            kiwi_values_list.append(int((kiwi_string.rsplit(': ', 1)[1]).rstrip()))
        except ValueError:
            print ('Kiwi Value either NULL or not valid integer \n{}'.format(kiwi_string))

    #This snippet checks directory and renamed it with datetimestam
    try:
       if os.path.exists('Dir1'):
           print 'Directory present'
           for i in range(5):
               renameDir("Dir"+str(i))

           #Sort direcotories
           sort_directory = sorted(directory_list)
           #print sort_directory
           
           #Assemble files
           with open('assembled.log', 'w') as outfile:
               for directory in sort_directory:
                   with open(directory + "/fruit.log") as infile:
                       for line in infile:
                           outfile.write(line)
                           if 'Kiwi' in line:
                               kiwi_values(line)
    except IOError:
        print("Five logs files not found.")
   
    #Minimum, Maximum and Average values of kiwi.
    if kiwi_values_list:
        print "min value of kiwi : ", min(kiwi_values_list)
        print "max value of kiwi : ", max(kiwi_values_list)
        print "average value of kiwi's: ", sum(kiwi_values_list)/len(kiwi_values_list)
    else:
        print 'No Kiwi present in any of the log files'

if __name__== "__main__":
    main()
