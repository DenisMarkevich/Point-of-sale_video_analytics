class TrackableObject:
	def __init__(self, objectID, centroid,dt):
		# store the object ID, then initialize a list of centroids
		# using the current centroid
		self.objectID = objectID
		self.centroids = [centroid]
		self.dt = dt

		# initialize a boolean used to indicate if the object has
		# already been counted or not
		self.counted = False