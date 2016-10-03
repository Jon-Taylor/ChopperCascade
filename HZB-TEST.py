from ChopperCode import *
HZB_Chopper_WFM1 = DiscChopper(Name='HZB_Chopper_WFM1', Type='disc', Disk_Thickness=20.0, Radius=700.0, Speed=70,
                                MaxSpeed=14.0, Source_Frequency=14.0,
                                Sense_Of_Rotation='cw', FlightPath=28.3-21.7, Upstream_guide_opening=[25.0, 30.0], phase=17.2,
                                delay=0.0,
                                Downstream_guide_opening=[20, 20], Number_of_Cutouts=6, Cutout_depth=50.0,
                                offset_from_TDC=[89.2,148,202,253.5,300,344.85], Cutout_sector_angle=[10.9,15.3,19.3,23.01,26.46,29.7])

HZB_Chopper_WFM2 = DiscChopper(Name='HZB_Chopper_WFM2', Type='disc', Disk_Thickness=20.0, Radius=600.0, Speed=70,
                                MaxSpeed=14.0, Source_Frequency=14.0,
                                Sense_Of_Rotation='cw', FlightPath=(28.3+.1)-21.7, Upstream_guide_opening=[25.0, 30.0], phase=46,
                                delay=0.0,
                                Downstream_guide_opening=[20, 20], Number_of_Cutouts=6, Cutout_depth=50.0,
                                offset_from_TDC=[70,133.5,191.6,244.6,296.3,344.8], Cutout_sector_angle=[10.9,15.3,19.3,19.3,23,29.7])

HZB_Chopper_FOL1 = DiscChopper(Name='HZB_Chopper_FOL1', Type='disc', Disk_Thickness=20.0, Radius=700.0, Speed=56,
                               MaxSpeed=14.0, Source_Frequency=14.0,
                               Sense_Of_Rotation='cw', FlightPath=30.5-21.7, Upstream_guide_opening=[25.0, 30.0], phase=32,
                               delay=0.0,
                               Downstream_guide_opening=[20, 20], Number_of_Cutouts=6, Cutout_depth=50.0,
                               offset_from_TDC=[74.6,139.6,194.3,245.3,294.8,347.2], Cutout_sector_angle=[20.6,23.2,21.8,17.8,15.7,24.4])

HZB_Chopper_DC2a = DiscChopper(Name='HZB_Chopper_DC2a', Type='disc', Disk_Thickness=20.0, Radius=700.0, Speed=14.0,
                               MaxSpeed=14.0, Source_Frequency=14.0,
                               Sense_Of_Rotation='cw', FlightPath=31.7-21.7, Upstream_guide_opening=[25.0, 30.0], phase=90,
                               delay=0.0,
                               Downstream_guide_opening=[20, 20], Number_of_Cutouts=1, Cutout_depth=50.0,
                               offset_from_TDC=[70], Cutout_sector_angle=[140])

HZB_Chopper_DC2b = DiscChopper(Name='HZB_Chopper_DC2b', Type='disc', Disk_Thickness=20.0, Radius=600.0, Speed=14.0,
                               MaxSpeed=14.0, Source_Frequency=14.0,
                               Sense_Of_Rotation='cw', FlightPath=32.3-21.7, Upstream_guide_opening=[25.0, 30.0], phase=90,
                               delay=0.0,
                               Downstream_guide_opening=[20, 20], Number_of_Cutouts=1, Cutout_depth=50.0,
                               offset_from_TDC=[101], Cutout_sector_angle=[202])

HZB_Chopper_FOL2 = DiscChopper(Name='HZB_Chopper_FOL2', Type='disc', Disk_Thickness=20.0, Radius=600.0, Speed=28,
                               MaxSpeed=14.0, Source_Frequency=14,
                               Sense_Of_Rotation='cw', FlightPath=37.6-21.7, Upstream_guide_opening=[25.0, 30.0], phase=20,
                               delay=0.0,
                               Downstream_guide_opening=[20, 20], Number_of_Cutouts=6, Cutout_depth=50.0,
                               offset_from_TDC=[98,154,206.8,254,299,344.65], Cutout_sector_angle=[36.6,36.06,30.21,26.88,24.56,29.11])


#Choppers2=[HZB_Chopper_WFM1,HZB_Chopper_WFM2,HZB_Chopper_FOL1,HZB_Chopper_DC2a,HZB_Chopper_DC2b,HZB_Chopper_FOL2]


Choppers2=[HZB_Chopper_WFM1,HZB_Chopper_WFM2,HZB_Chopper_FOL2]


Calculate_chopper_cascade_Time_Distance(Choppers2)

print HZB_Chopper_WFM1.Chopper_Opening_Times


print HZB_Chopper_WFM2.Chopper_Opening_Times

print HZB_Chopper_FOL2.Chopper_Opening_Times

Calculate_Cascade_Transmission(Choppers=Choppers2,Number_of_Frames=1)