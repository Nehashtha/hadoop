1. Download input file and load it into HDFS

    command to copy file from local host to Haddop file system
    
    a. $hadoop fs -put file_name_in_localFS /<dir_in_hdfs>
    b. $hadoop fs -copyfromlocal file_name_in_localFS /<dir_in_hdfs> 
    
2. To run hadoop program we need to open terminal in administrative mode and change direcry to “c:\hadoop-2.7.7\sbin” and type “startall.cmd” to start apache hadoop. 
    Following apps must be running in background 
        • Hadoop Namenode 
        • Hadoop datanode
        • Yarn Node manager 
        • Yarn resource manager 
        
3. Java programming is used to write the Hadoop framework so, to run the map reduce code in another language like python, Ruby and rails, R  etc.
   we use Hadoop streaming.
   
   Command for hadoop streaming
   
   a. hadoop jar hadoop-streaming-2.7.7.jar 
      -D mapred.map.tasks=4  
      -file <path_to_mapper.py>  
      -mapper "python <path_to_a2mapper.py>"   
      -file <path_to_a2_reducer.py>  
      -reducer "python <path_to_a2_reducer.py>"  
      -input <path_to_inputfile_in_hdfs>  
      -output <path_to_store_result_in_hdfs> 
      
      Here 4 mapper is Used and absolute path of Python should be defined in system variable PATH .
      
   
