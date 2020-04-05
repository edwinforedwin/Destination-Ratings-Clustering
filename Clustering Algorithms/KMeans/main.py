#KMeans Clustering

kmean = KMeans(n_clusters=2, random_state=0).fit(X)
y_kmeans = kmean.predict(X)
lab = kmean.labels_
#for i in range(1,10):
plt.figure(figsize=(14,7))
plt.title("KMeans Clustering on Destinations Rating",fontsize=20)
plt.scatter(X[:,0], X[:,1],c = y_kmeans, s=80, cmap='cividis',alpha=0.8,marker='H')
plt.xlabel("X Axis Rating")
plt.ylabel("Y Axis Rating")
plt.show()
