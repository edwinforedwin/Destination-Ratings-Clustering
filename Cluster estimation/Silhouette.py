#Silhouette Method

no_of_clusters = [2, 3, 4, 5, 6] 
print("Average Silhouette Method\n")
for n_clusters in no_of_clusters: 
  
    cluster = KMeans(n_clusters = n_clusters) 
    cluster_labels = cluster.fit_predict(X) 
  
    # The silhouette_score gives the  
    # average value for all the samples. 
    silhouette_avg = silhouette_score(X, cluster_labels) 
  
    print("For no of clusters =", n_clusters," The average silhouette_score is :", silhouette_avg) 
