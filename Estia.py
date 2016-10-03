from ChopperCode import *

EstiaCh1 = DiscChopper(Name='EstiaCh1', Type='disc', Disk_Thickness=20.0, Radius=300.0, Speed=14.0, MaxSpeed=14.0,
                            Source_Frequency=14.0,
                            Sense_Of_Rotation='cw', FlightPath=10.84, Upstream_guide_opening=[25.0, 30.0], phase=0.0,
                            delay=0.0,
                            Downstream_guide_opening=[20, 20], Number_of_Cutouts=2, Cutout_depth=50.0,
                            offset_from_TDC=[90], Cutout_sector_angle=[100.06])




Choppers = [EstiaCh1]

Calculate_chopper_cascade_Time_Distance(Choppers)

lambda_with_transmission,histogram=Calculate_Cascade_Transmission(Choppers=Choppers,Number_of_Frames=4)
