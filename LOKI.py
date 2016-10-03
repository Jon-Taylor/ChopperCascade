from ChopperCode import DiscChopper, Calculate_Cascade_Transmission,Lambda_To_Time,Calculate_chopper_cascade_Time_Distance
import matplotlib.pyplot as plt
import numpy as np

LOKI_Chopper1 = DiscChopper(Name='test', Type='disc', Disk_Thickness=20.0, Radius=300.0, Speed=14.0, MaxSpeed=14.0,
                            Source_Frequency=14.0,
                            Sense_Of_Rotation='cw', FlightPath=6.5, Upstream_guide_opening=[25.0, 30.0], phase=65.0,
                            delay=0.0,
                            Downstream_guide_opening=[20, 20], Number_of_Cutouts=2, Cutout_depth=50.0,
                            offset_from_TDC=[0], Cutout_sector_angle=[120])

LOKI_Chopper2 = DiscChopper(Name='test', Type='disc', Disk_Thickness=20.0, Radius=300.0, Speed=14.0, MaxSpeed=14.0,
                            Source_Frequency=14.0,
                            Sense_Of_Rotation='cw', FlightPath=6.67, Upstream_guide_opening=[25.0, 30.0], phase=65.0,
                            delay=0.0,
                            Downstream_guide_opening=[20, 20], Number_of_Cutouts=4, Cutout_depth=50.0,
                            offset_from_TDC=[0], Cutout_sector_angle=[120])

LOKI_Chopper3 = DiscChopper(Name='test', Type='disc', Disk_Thickness=20.0, Radius=300.0, Speed=14.0, MaxSpeed=14.0,
                            Source_Frequency=14.0,
                            Sense_Of_Rotation='cw', FlightPath=11.5, Upstream_guide_opening=[25.0, 30.0], phase=85.0,
                            delay=0.0,
                            Downstream_guide_opening=[20, 20], Number_of_Cutouts=2, Cutout_depth=50.0,
                            offset_from_TDC=[0], Cutout_sector_angle=[160])

LOKI_Chopper4 = DiscChopper(Name='test', Type='disc', Disk_Thickness=20.0, Radius=300.0, Speed=14.0, MaxSpeed=14.0,
                            Source_Frequency=14.0,
                            Sense_Of_Rotation='cw', FlightPath=11.67, Upstream_guide_opening=[25.0, 30.0], phase=85.0,
                            delay=0.0,
                            Downstream_guide_opening=[20, 20], Number_of_Cutouts=4, Cutout_depth=50.0,
                            offset_from_TDC=[0], Cutout_sector_angle=[160])


Choppers = [LOKI_Chopper1, LOKI_Chopper2, LOKI_Chopper3, LOKI_Chopper4]

Calculate_chopper_cascade_Time_Distance(Choppers)

lambda_with_transmission,histogram=Calculate_Cascade_Transmission(Choppers=Choppers,Number_of_Frames=1)


#TOF_at_sample = Lambda_To_Time(lambda_with_transmission,22)

