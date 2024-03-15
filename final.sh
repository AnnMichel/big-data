
# Copy output files from container to local machine
docker cp bd-a1-container2:/home/doc-bd-a1/res_dpre.csv C:/Users/ann_a/bd-a1/service-result/
docker cp bd-a1-container2:/home/doc-bd-a1/eda-in-1.txt C:/Users/ann_a/bd-a1/service-result/
docker cp bd-a1-container2:/home/doc-bd-a1/eda-in-2.txt C:/Users/ann_a/bd-a1/service-result/
docker cp bd-a1-container2:/home/doc-bd-a1/eda-in-3.txt C:/Users/ann_a/bd-a1/service-result/
docker cp bd-a1-container2:/home/doc-bd-a1/k.txt C:/Users/ann_a/bd-a1/service-result/
docker cp bd-a1-container2:/home/doc-bd-a1/vis.png C:/Users/ann_a/bd-a1/service-result/

# Stop the container
docker stop bd-a1-container2

