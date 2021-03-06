import open3d as o3d
import matplotlib.pyplot as plt
 

dir = ""
if __name__ == "__main__":
    print("Read Redwood dataset")
    color_raw = o3d.io.read_image("./data/rgb/1626941990.867689.png")
    depth_raw = o3d.io.read_image("./data/depth/1626941990.867689.png")
    rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(
        color_raw, depth_raw)
    # print(rgbd_image)
 
    # plt.subplot(1, 2, 1)
    # plt.title('grayscale image')
    # plt.imshow(rgbd_image.color)
    # plt.subplot(1, 2, 2)
    # plt.title('depth image')
    # plt.imshow(rgbd_image.depth)
    # plt.show()
 
    pcd = o3d.geometry.PointCloud.create_from_rgbd_image(
        rgbd_image,
        o3d.camera.PinholeCameraIntrinsic(
            o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault))
    # Flip it, otherwise the pointcloud will be upside down
    pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
    o3d.io.write_point_cloud("test.pcd", pcd)
    o3d.visualization.draw_geometries([pcd])