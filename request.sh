
for var in 0 1 2 3
do
 
curl -i -H "Accept: application/json" -H "Content-Type: application/json" GET https://api.thingspeak.com/talkbacks/your_customer_id/commands/execute.json?api_key=your_API_key | json command_string > output.txt


sed '1,19d' output.txt >> newoutput.txt

done

a=`cat newoutput.txt`


vlc $a
