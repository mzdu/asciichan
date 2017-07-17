counter=10

for((i=0;i<counter;i=i+2));do
    python time_now.py | while read line; do
        if [ "${line}" == "time_now" ]; then 
            echo "working" 
	    echo $i
        fi
        
    done
done
