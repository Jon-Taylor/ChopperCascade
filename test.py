from ChopperCode import *
test = DiscChopper(Name='test', Type='disc', Disk_Thickness=20.0, Radius=700.0, Speed=14,
                                MaxSpeed=14.0, Source_Frequency=14,
                                Sense_Of_Rotation='cw', FlightPath=20, Upstream_guide_opening=[25.0, 30.0], phase=100,
                                delay=0.0,
                                Downstream_guide_opening=[20, 20], Number_of_Cutouts=1, Cutout_depth=50.0,
                                offset_from_TDC=[0,90,180,270], Cutout_sector_angle=[10,20,30,40])

HZB_Chopper_FOL2 = DiscChopper(Name='HZB_Chopper_FOL2', Type='disc', Disk_Thickness=20.0, Radius=600.0, Speed=28,
                               MaxSpeed=14.0, Source_Frequency=14,
                               Sense_Of_Rotation='cw', FlightPath=37.6 - 21.7, Upstream_guide_opening=[25.0, 30.0],
                               phase=300,
                               delay=0.0,
                               Downstream_guide_opening=[20, 20], Number_of_Cutouts=6, Cutout_depth=50.0,
                               offset_from_TDC=[98, 154, 206.8, 254, 299, 344.65],
                               Cutout_sector_angle=[36.6, 36.06, 30.21, 26.88, 24.56, 29.11])

Choppers2=[HZB_Chopper_FOL2]

Calculate_chopper_cascade_Time_Distance(Choppers2)