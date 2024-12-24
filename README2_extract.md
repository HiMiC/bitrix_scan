



cd uploads

mkdir -p ../uploads_sources/birix24_shop_encode
tar -xvzf bitrix24_shop_encode.tar.gz -C ../uploads_sources/birix24_shop_encode

mkdir -p ../uploads_sources/business_cluster_postgresql_encode
tar -xvzf business_cluster_postgresql_encode.tar.gz -C ../uploads_sources/business_cluster_postgresql_encode

mkdir -p ../uploads_sources/business_encode
tar -xvzf business_encode.tar.gz -C ../uploads_sources/business_encode

mkdir -p ../uploads_sources/small_business_encode
tar -xvzf small_business_encode.tar.gz -C ../uploads_sources/small_business_encode

mkdir -p ../uploads_sources/standard_encode
tar -xvzf standard_encode.tar.gz -C ../uploads_sources/standard_encode

mkdir -p ../uploads_sources/start_encode
tar -xvzf start_encode.tar.gz -C ../uploads_sources/start_encode

===============

cat start_encode.json | jq | grep "./bitrix/modules/" | wc -l
cat standard_encode.json | jq | grep "./bitrix/modules/" | wc -l
cat small_business_encode.json | jq | grep "./bitrix/modules/" | wc -l
cat business_encode.json | jq | grep "./bitrix/modules/" | wc -l
cat bitrix24_shop_encode.json | jq | grep "./bitrix/modules/" | wc -l
cat business_cluster_postgresql_encode.json | jq | grep "./bitrix/modules/" | wc -l


13130
16788
26778
36003
63099
32843

================

cat start_encode.json | jq | grep "./bitrix/modules/" >> modules_file2.txt
cat standard_encode.json | jq | grep "./bitrix/modules/" >> modules_file2.txt
cat small_business_encode.json | jq | grep "./bitrix/modules/" >> modules_file2.txt
cat business_encode.json | jq | grep "./bitrix/modules/" >> modules_file2.txt
cat bitrix24_shop_encode.json | jq | grep "./bitrix/modules/" >> modules_file2.txt
cat business_cluster_postgresql_encode.json | jq | grep "./bitrix/modules/" >> modules_file2.txt

cat modules_file2.txt |sort -u > modules_file.txt



