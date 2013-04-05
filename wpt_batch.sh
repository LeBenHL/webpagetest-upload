urls=$1
device=$2
numberOfPhones=$3
now=$(date +"DATE_%m_%d_%y_TIME_%I_%M_%S_%p")

totalLines=$(cat ${urls} | wc -l)
((linesPerFile = (totalLines + numberOfPhones - 1) / numberOfPhones))
prefix=/urls.

mkdir "$now"
split -a 2 -l $linesPerFile $urls "$now$prefix"

urlFiles="$now"/*

count=1
for urlFile in $urlFiles
do
	echo Processing $urlFile on $device-"$count"
	python wpt_batch.py --server=http://www.benjaminhoanle.com/ --outputdir="$now/" --urlfile=$urlFile --tcpdump --location=$device-"$count" --runs=1 &
	count=$((count+1))
done

