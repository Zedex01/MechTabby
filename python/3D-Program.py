import open3d as o3d

#create empty scene
empty_scene = []

pcd = o3d.io.read_point_cloud("Gemstone.ply")

pcd.paint_uniform_color([0.1, 0.8, 0.1])  # green-ish

#open the viewer
o3d.visualization.draw_geometries([pcd])


