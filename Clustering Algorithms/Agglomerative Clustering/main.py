model = AgglomerativeClustering(distance_threshold=0, n_clusters=None)

model = model.fit(X)
plt.figure(figsize=(14,7))
plt.title('Hierarchical Clustering Dendrogram')
# plot the top three levels of the dendrogram
plot_dendrogram(model, truncate_mode='level', p=3)
plt.xlabel("Number of points in node (or index of point if no parenthesis).")
plt.show()

y_agg = model.fit_predict(X)

plt.figure(figsize=(14,7))
plt.title("Agglomerative Clustering on Destinations Rating",fontsize=20)
plt.scatter(X[:,0], X[:,1],c = y_agg, s=80, cmap='cividis',alpha=0.5,marker='H')
plt.xlabel("X Axis Rating")
plt.ylabel("Y Axis Rating")
plt.show()
