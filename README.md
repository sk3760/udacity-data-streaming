# udacity-data-streaming
SF Crime Statistics with Spark Streaming

1. How did changing values on the SparkSession property parameters affect the throughput and latency of the data?
Changing the Spark configuration option *maxRatePerPartition* changes the maximum number of messages per partition per batch. The higher the number for this, the more messages per partition per batch are allowed. Also, changing the *maxOffsetsPerTrigger* option limits the number of records to fetch per trigger. Again, the higher the number, the more records can be fetched per trigger. 

2. What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?
I think the two that I mentioned above are very efficient (maxRatePerPartition and maxOffsetsPerTrigger). These values stop spark streaming from getting overwhelmed with data (stops memory overload). If spark gets overwhelmed with data and runs out of memory, the whole job will fail, so these options are extremely imporant when doing data streaming. 
