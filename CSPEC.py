from ChopperCode import DiscChopper, Calculate_Cascade_Transmission, Lambda_To_Time, Phase_chopper_cascade, \
    Calculate_chopper_cascade_Time_Distance
import matplotlib.pyplot as plt
import numpy as np

R = 2

N1 = -(3 - 21) * 14
N2 = -(4 - 28) * 14

Npr = N2 * (R - 1) / R

Fm = N2 * 14
Fp = .75 * N2 * 14
print 'N1,N2,Npr,Fm,Fp'
print N1, N2, Npr, Fm, Fp

CSPEC_Chopper_BW1 = DiscChopper(Name='CSPEC_Chopper_BW1', Type='disc', Disk_Thickness=20.0, Radius=700.0, Speed=14.0,
                                MaxSpeed=14.0, Source_Frequency=14.0,
                                Sense_Of_Rotation='cw', FlightPath=18.6, Upstream_guide_opening=[25.0, 30.0], phase=17,
                                delay=0.0,
                                Downstream_guide_opening=[20, 20], Number_of_Cutouts=2, Cutout_depth=50.0,
                                offset_from_TDC=[0], Cutout_sector_angle=[35.7])

CSPEC_Chopper_BW2 = DiscChopper(Name='CSPEC_Chopper_BW2', Type='disc', Disk_Thickness=20.0, Radius=600.0, Speed=14.0,
                                MaxSpeed=14.0, Source_Frequency=14.0,
                                Sense_Of_Rotation='cw', FlightPath=32.75, Upstream_guide_opening=[25.0, 30.0], phase=5,
                                delay=0.0,
                                Downstream_guide_opening=[20, 20], Number_of_Cutouts=4, Cutout_depth=50.0,
                                offset_from_TDC=[0], Cutout_sector_angle=[63.26])

CSPEC_Chopper_P1 = DiscChopper(Name='CSPEC_Chopper_P1', Type='disc', Disk_Thickness=20.0, Radius=700.0, Speed=252.0,
                               MaxSpeed=14.0, Source_Frequency=14.0,
                               Sense_Of_Rotation='cw', FlightPath=100, Upstream_guide_opening=[25.0, 30.0], phase=0,
                               delay=0.0,
                               Downstream_guide_opening=[20, 20], Number_of_Cutouts=2, Cutout_depth=50.0,
                               offset_from_TDC=[0, 180], Cutout_sector_angle=[41, 41])

CSPEC_Chopper_P2 = DiscChopper(Name='CSPEC_Chopper_P2', Type='disc', Disk_Thickness=20.0, Radius=700.0, Speed=252.0,
                               MaxSpeed=14.0, Source_Frequency=14.0,
                               Sense_Of_Rotation='cw', FlightPath=100.025, Upstream_guide_opening=[25.0, 30.0], phase=5,
                               delay=0.0,
                               Downstream_guide_opening=[20, 20], Number_of_Cutouts=4, Cutout_depth=50.0,
                               offset_from_TDC=[0, 180], Cutout_sector_angle=[41, 41])

CSPEC_Chopper_PR = DiscChopper(Name='CSPEC_Chopper_PR', Type='disc', Disk_Thickness=20.0, Radius=600.0, Speed=168.0,
                               MaxSpeed=14.0, Source_Frequency=14.0,
                               Sense_Of_Rotation='cw', FlightPath=149.95, Upstream_guide_opening=[25.0, 30.0], phase=0,
                               delay=0.0,
                               Downstream_guide_opening=[20, 20], Number_of_Cutouts=2, Cutout_depth=50.0,
                               offset_from_TDC=[0], Cutout_sector_angle=[5.33])

CSPEC_Chopper_M1 = DiscChopper(Name='CSPEC_Chopper_M1', Type='disc', Disk_Thickness=20.0, Radius=600.0, Speed=336.0,
                               MaxSpeed=14.0, Source_Frequency=14.0,
                               Sense_Of_Rotation='cw', FlightPath=149.975, Upstream_guide_opening=[25.0, 30.0], phase=5,
                               delay=0.0,
                               Downstream_guide_opening=[20, 20], Number_of_Cutouts=4, Cutout_depth=50.0,
                               offset_from_TDC=[0], Cutout_sector_angle=[5.33])

CSPEC_Chopper_M2 = DiscChopper(Name='CSPEC_Chopper_M2', Type='disc', Disk_Thickness=20.0, Radius=600.0, Speed=336.0,
                               MaxSpeed=14.0, Source_Frequency=14.0,
                               Sense_Of_Rotation='cw', FlightPath=150, Upstream_guide_opening=[25.0, 30.0], phase=5,
                               delay=0.0,
                               Downstream_guide_opening=[20, 20], Number_of_Cutouts=2, Cutout_depth=50.0,
                               offset_from_TDC=[0], Cutout_sector_angle=[5.33])

Choppers2 = [CSPEC_Chopper_BW1, CSPEC_Chopper_BW2, CSPEC_Chopper_P1, CSPEC_Chopper_P2, CSPEC_Chopper_PR,
             CSPEC_Chopper_M1, CSPEC_Chopper_M2]

Phase_chopper_cascade(Choppers=Choppers2, LambdaSet=2)


Calculate_chopper_cascade_Time_Distance(Choppers2)


#Calculate_Cascade_Transmission(Choppers=Choppers2,Number_of_Frames=7)

# lambda_with_transmission,histogram=Calculate_Cascade_Transmission(Choppers=Choppers2,Number_of_Frames=4)
# plt.plot(lambda_with_transmission,histogram)
# plt.show()

#plt.figure()
#plt.show()
#Calculate_Cascade_Transmission(Choppers=Choppers2, Number_of_Frames=4)

# TOF_at_sample = Lambda_To_Time(lambda_with_transmission,151)
