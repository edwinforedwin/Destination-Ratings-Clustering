#Affinity Propogation Clustering

af = AffinityPropagation(preference=-500).fit(X)
cluster_centers_indices = af.cluster_centers_indices_
labels = af.labels_

n_clusters_ = len(cluster_centers_indices)
plt.figure(figsize=(14,7))

colors = cycle('gmrcbykgmrcbykgmrcbykgmrcbyk')
for k, col in zip(range(n_clusters_), colors):
    class_members = labels == k
    cluster_center = X[cluster_centers_indices[k]]
    plt.plot(X[class_members, 0], X[class_members, 1], col + '.')
    plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
             markeredgecolor='k', markersize=14)
    for x in X[class_members]:
        plt.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)

plt.xlabel("X Axis Rating")
plt.ylabel("Y Axis Rating")
plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()

y_ac = af.predict(X)
plt.figure(figsize=(14,7))
plt.title("Affinity Clustering on Destinations Rating",fontsize=20)
plt.scatter(X[:,0], X[:,1],c = y_ac, s=80, cmap='cividis',alpha=0.5,marker='H')
plt.xlabel("X Axis Rating")
plt.ylabel("Y Axis Rating")
plt.show()
