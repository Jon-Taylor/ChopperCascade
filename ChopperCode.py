import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math


class DiscChopper:
    def __init__(self, Name=None, Type=None, Disk_Thickness=None, Radius=None, Speed=None, MaxSpeed=None,
                 Source_Frequency=None,
                 Sense_Of_Rotation=None, FlightPath=None, Upstream_guide_opening=None, phase=None, delay=None,
                 Downstream_guide_opening=None, Number_of_Cutouts=None, Cutout_depth=None, offset_from_TDC=None,
                 Cutout_sector_width=None,
                 Cutout_sector_angle=None):
        self.Name = Name
        self.Type = Type
        self.Disk_Thickness = Disk_Thickness
        self.Radius = Radius
        self.Speed = Speed
        self.MaxSpeed = MaxSpeed
        self.Source_Frequency = Source_Frequency
        self.Sense_Of_Rotation = Sense_Of_Rotation
        self.FlightPath = FlightPath
        self.Upstream_guide_opening = Upstream_guide_opening  # WxH
        self.Downstream_guide_opening = Downstream_guide_opening
        self.phase = phase
        self.delay = delay
        # Type (sector)
        # Number 1

        self.Number_of_Cutouts = Number_of_Cutouts

        self.Cutout_depth = Cutout_depth
        self.offset_from_TDC = offset_from_TDC
        self.Cutout_sector_width = Cutout_sector_width
        self.Cutout_sector_angle = Cutout_sector_angle
        self.offsets_at_speed = None
        self.Offset_Time_From_Angle = None
        self.Cutout_sector_angle_at_speed = None
        self.Burst_Time_centre = None
        self.Total_transmission_Time = None
        self.FrameTime = None
        self.Chopper_Data = None
        self.Chopper_Opening_Times = None
        self.Chopper_Closing_Times = None
        self.Chopper_Data_for_Display = None

    def ToMetre(self, millimetere):
        return millimetere / 1000

    def ToMicroSec(self, Seconds):
        return Seconds * 1e6

    def Calulate_Omega(self, Speed):
        return 2.0 * math.pi * Speed

    def Calculate_Radius_at_Centre(self, Radius, Cutout_depth):
        return Radius - Cutout_depth / 2

    def Time_for_single_Rotation(self, omega):
        return self.ToMicroSec(2.0 * math.pi / omega)

    def Calulate_Delay_From_phase(self, phase, omega):
        return phase / omega

    def Calculate_Phase_From_Delay(self, delay, omega):
        return delay * omega

    def Calculate_Cutout_Angle(self, Cutout_sector_width, Radius, Cutout_depth):
        Radius_at_centre = Radius - Cutout_depth / 2
        Cutout_sector_angle = []
        for i in range(len(Cutout_sector_width)):
            Cutout_sector_angle.append((360.0 * Cutout_sector_width[i]) / (2 * math.pi * Radius_at_centre))
        return Cutout_sector_angle

    def Calculate_Source_multuplier(self, Speed, Source_Frequency):
        return Speed / Source_Frequency

    def Calculate_Offset_angles_At_Speed(self, offset_from_TDC, Source_Multiplier):

        tmpind=np.argsort(np.mod(np.array(offset_from_TDC)+self.phase,360))
        offset = np.sort(np.mod(np.array(offset_from_TDC)+self.phase,360))
        self.Cutout_sector_angle = list(np.array(self.Cutout_sector_angle)[tmpind])
        tmp=np.array([])
        for i in range(int(Source_Multiplier)):
            tmp=np.append(tmp,offset+(360*i))
        offsets_at_speed=tmp

        #if Source_Multiplier >= 1:
        #    deltas = np.array(
        #        [(a - b) for a, b in zip(offset_from_TDC[1:] + [360.0], offset_from_TDC)] * int(Source_Multiplier))
        #    print deltas
        #    offsets_at_speed = np.sort(np.fmod(deltas.cumsum(), 360.0 * Source_Multiplier))
        #if Source_Multiplier == 1:
        #    offsets_at_speed = np.array(offset_from_TDC)  #[:-len(offset_from_TDC) / 2]
        return offsets_at_speed

    def Calculate_offset_Time_From_Angle(self, offsets_at_speed, omega):
        Offset_Time_From_Angle = []
        for offset in offsets_at_speed:
            Offset_Time_From_Angle.append(self.ToMicroSec(math.radians(offset) / omega))
        return Offset_Time_From_Angle


    def Calculate_Cutout_Angle_at_Speed(self, Cutout_sector_angle, Source_Multiplier):

        Cutout_sector_angle_at_speed = []
        if Source_Multiplier < 1:
            Source_Multiplier = 1
        for i in range(int(Source_Multiplier)):
            for j in range(len(Cutout_sector_angle)):
                Cutout_sector_angle_at_speed.append(Cutout_sector_angle[j])

        return Cutout_sector_angle_at_speed

    def Calculate_Burst_Time_Centre(self, Cutout_sector_angle_at_speed, omega):
        Burst_Time_centre = []
        for i in range(len(Cutout_sector_angle_at_speed)):
            Burst_Time_centre.append(self.ToMicroSec(math.radians(Cutout_sector_angle_at_speed[i]) / omega))
        return Burst_Time_centre

    def Calculate_Total_transmission_Time(self, Cutout_sector_angle_at_speed, omega, Upstream_guide_opening,
                                          Radius_at_centre):
        Total_transmission_Time = []
        for i in range(len(Cutout_sector_angle_at_speed)):
            Total_transmission_Time.append(self.ToMicroSec(((1 / omega) * (
            math.radians(Cutout_sector_angle_at_speed[i]) + (2 * math.atan(
                (self.ToMetre(Upstream_guide_opening[0]) * .5) / (
                self.ToMetre(Radius_at_centre) - self.ToMetre(Upstream_guide_opening[1] * .5))))))))

        return Total_transmission_Time

    def Calculate_Time_For_Full_transmission(self, Cutout_sector_angle_at_speed, omega, Upstream_guide_opening,
                                             Radius_at_centre):
        Time_For_Full_transmission = []
        for i in range(len(Cutout_sector_angle_at_speed)):
            Time_Full_transmission.append(self.ToMicroSec((1 / omega) * (
            math.radians(Cutout_sector_angle_at_speed[i]) - (2 * math.atan((ToMetre(Upstream_guide_opening[0]) * .5) / (
            ToMetre(Radius_at_centre) - ToMetre(Upstream_guide_opening[1] * .5)))))))

    def Calculate_Frame_Time(self, Source_Frequency):
        FrameTime = [0]
        End_of_Frame = self.ToMicroSec(1.0 / Source_Frequency)
        FrameTime.append(End_of_Frame)
        return FrameTime

    def Generate_Chopper_data_for_Display(self, Chopper_opening, Chopper_closing, FrameTime):
        Chopper_Data = []
        for i in range(len(Chopper_opening) - 1):
            Chopper_Data.append([Chopper_closing[i], Chopper_opening[i + 1]])
        if Chopper_opening[0] < 0:
            Chopper_Data.append([Chopper_closing[-1], FrameTime[1] + Chopper_opening[0]])
        if Chopper_opening[0] > 0:
            Chopper_Data.append([Chopper_closing[-1], FrameTime[1]])
            Chopper_Data.append([FrameTime[0], Chopper_opening[0]])

        return Chopper_Data

    def Generate_Chopper_data(self, Chopper_opening, Total_transmission_Time, FrameTime):
        Chopper_Data = []
        for i in range(len(Chopper_opening)):
            Chopper_Data.append([Chopper_opening[i], Chopper_opening[i] + Total_transmission_Time[i]])
        return Chopper_Data

    def Display_Chopper_Data(self,axisHandle):

        for i in range(len(self.Chopper_Data_for_Display)):
            axisHandle.plot(self.Chopper_Data_for_Display[i], [self.FlightPath, self.FlightPath], 'b')

        axisHandle.set_xlim(self.FrameTime)
        axisHandle.set_ylim([0, self.FlightPath * 1.2])

    def Calculate_Chopper_Opening_Times(self, Offset_Time_At_Speed, Total_transmission_Time):
        Chopper_Opening_Times = []
        for i in range(len(Offset_Time_At_Speed)):
            Chopper_Opening_Times.append(Offset_Time_At_Speed[i] - (Total_transmission_Time[i] / 2.0))
        return Chopper_Opening_Times

    def Calculate_Chopper_Closing_Times(self, Offset_Time_At_Speed, Total_transmission_Time):
        Chopper_Closing_Times = []
        for i in range(len(Offset_Time_At_Speed)):
            Chopper_Closing_Times.append(Offset_Time_At_Speed[i] + (Total_transmission_Time[i] / 2.0))
        return Chopper_Closing_Times

    def Calculate_Chopper_Time_strucure(self):

        Radius_at_centre = self.Calculate_Radius_at_Centre(self.Radius, self.Cutout_depth)

        self.omega = self.Calulate_Omega(self.Speed)

        if self.Cutout_sector_angle is None:
            self.Cutout_sector_angle = self.Calculate_Cutout_Angle(self.Cutout_sector_width, self.Radius, self.Cutout_depth)

        Source_Multiplier = self.Calculate_Source_multuplier(self.Speed, self.Source_Frequency)

        self.offsets_at_speed = self.Calculate_Offset_angles_At_Speed(self.offset_from_TDC, Source_Multiplier)


        self.Cutout_sector_angle_at_speed = self.Calculate_Cutout_Angle_at_Speed(self.Cutout_sector_angle, Source_Multiplier)

        self.Total_transmission_Time = self.Calculate_Total_transmission_Time(self.Cutout_sector_angle_at_speed, self.omega,
                                                                         self.Upstream_guide_opening, Radius_at_centre)

        self.Offset_Time_At_Speed = self.Calculate_offset_Time_From_Angle(self.offsets_at_speed, self.omega)

        self.FrameTime = self.Calculate_Frame_Time(self.Source_Frequency)


        self.Chopper_Opening_Times = self.Calculate_Chopper_Opening_Times(self.Offset_Time_At_Speed, self.Total_transmission_Time)


        self.Chopper_Closing_Times = self.Calculate_Chopper_Closing_Times(self.Offset_Time_At_Speed, self.Total_transmission_Time)

        self.Chopper_Data_for_Display = self.Generate_Chopper_data_for_Display(self.Chopper_Opening_Times, self.Chopper_Closing_Times,
                                                                          self.FrameTime)

        self.Chopper_Data = self.Generate_Chopper_data(self.Chopper_Opening_Times, self.Total_transmission_Time, self.FrameTime)


def lambda_time_at_first_chopper(Number_of_Frames=None, FlighPath=None):
    TOF_Max = (Number_of_Frames / 14.0) * 1e6
    TOF_Min = 1.0
    lambda_Min = TOF_Min / ((252.82 * FlighPath))
    lambda_Max = TOF_Max / ((252.82 * FlighPath))
    print lambda_Min, lambda_Max
    Delta_Lambda = ((lambda_Max - lambda_Min) / TOF_Max)*30

    lam = np.arange(lambda_Min, lambda_Max, Delta_Lambda)

    accel_Time = np.arange(0, 3000, 1)

    timeAtChopper_from_lam = np.zeros((len(accel_Time), len(lam)))

    for i in range(len(accel_Time)):
        timeAtChopper_from_lam[i, :] = (252.82 * lam * FlighPath) + accel_Time[i]

    return timeAtChopper_from_lam, lam


def calculate_transmitted_lambda(Chopper_Obj=None, Number_of_Frames=None, timeAtChopper_from_lam=None, Lambda=None,
                                 histogram_in=None):
    Chopper_Times_min = []
    Chopper_Times_max = []
    Chopper_Times_min = np.array(Chopper_Obj.Chopper_Opening_Times)
    Chopper_Times_max = np.array(Chopper_Obj.Chopper_Closing_Times)
    FlightPath = Chopper_Obj.FlightPath

    single_frame_openings = len(Chopper_Times_min)

    if Number_of_Frames > 1:
        for i in range(int(Number_of_Frames) - 1):
            Chopper_Times_min = np.append(Chopper_Times_min, [Chopper_Times_min[-single_frame_openings:] + 72000])
            Chopper_Times_max = np.append(Chopper_Times_max, [Chopper_Times_max[-single_frame_openings:] + 72000])


    lambda_with_transmission = []
    histogram = []

    if len(timeAtChopper_from_lam.shape) > 1:
        for j in range(len(Chopper_Times_min)):
            print '########## Opening ', j, '###################'
            for i in range(len(Lambda)):
                index2 = np.where(np.logical_and(timeAtChopper_from_lam[:, i] > Chopper_Times_min[j],
                                                 timeAtChopper_from_lam[:, i] < Chopper_Times_max[j]))

                if len(index2[0]) > 0:
                    histogram.append(len(index2[0]))
                    lambda_with_transmission.append(Lambda[i])
                    # print Lambda[i],len(index2[0])
    if len(timeAtChopper_from_lam.shape) == 1:
        for j in range(len(Chopper_Times_min)):
            print '########## Opening ', j, '###################'
            for i in range(len(Lambda)):
                index2 = np.where(np.logical_and(timeAtChopper_from_lam[i] > Chopper_Times_min[j],
                                                 timeAtChopper_from_lam[i] < Chopper_Times_max[j]))

                if len(index2[0]) > 0:
                    histogram.append(histogram_in[i])
                    lambda_with_transmission.append(Lambda[i])
                    # print Lambda[i],len(index2[0])
    return lambda_with_transmission, histogram

def Lambda_To_Time(Lambda=None, FlightPath=None):
    TOF = []
    for Lam in Lambda:
        TOF.append(252.82 * Lam * FlightPath)
    TOF = np.array(TOF)
    return TOF


def Plot_Lambda_Transmission(lambda_with_transmission, histogram,headings):
    #newX, newY = rebin(lambda_with_transmission, histogram)
    plt.figure()
    plt.plot(lambda_with_transmission, histogram, '-',lw=3)
    plt.title(headings[0])
    plt.show()

def rebin(xdata,ydata):
    xarray = np.array(xdata)
    yarray = np.array(ydata)

    newX = np.linspace(0.0, xarray.max(), 5000)

    newY = np.zeros(newX.shape)

    inds = np.digitize(xarray, newX)

    newY[inds - 1] = ydata
    return newX, newY


def Calculate_Cascade_Transmission(Choppers=None, Number_of_Frames=None):
    timeAtChopper_from_lam, lam = lambda_time_at_first_chopper(Number_of_Frames=Number_of_Frames,
                                                               FlighPath=Choppers[0].FlightPath)

    print timeAtChopper_from_lam.shape
    print lam.shape

    lambda_with_transmission, histogram = calculate_transmitted_lambda2(Choppers[0], Number_of_Frames,
                                                                       timeAtChopper_from_lam, lam)


    Plot_Lambda_Transmission(lambda_with_transmission, histogram,['transmitted Lambda for chopper at '+str(Choppers[0].FlightPath)+' m'])

    for chopper in Choppers[1:]:
        TOF = Lambda_To_Time(lambda_with_transmission, chopper.FlightPath)
        lambda_with_transmission, histogram = calculate_transmitted_lambda2(chopper, Number_of_Frames, TOF,
                                                                           lambda_with_transmission, histogram)

        Plot_Lambda_Transmission(lambda_with_transmission, histogram,['transmitted Lambda for chopper at '+str(chopper.FlightPath)+' m'])

    return lambda_with_transmission, histogram


def Calculate_chopper_cascade_Time_Distance(Choppers=None):
    ax = plt.gca()
    for chopperObjcet in Choppers:
        chopperObjcet.Calculate_Chopper_Time_strucure()
        chopperObjcet.Display_Chopper_Data(ax)
    plt.show()


def Phase_chopper_cascade(Choppers=None, LambdaSet=None):
    for chopperObjcet in Choppers:
        degPerSec = chopperObjcet.Speed * 360
        PhaseAngle = degPerSec * ((Lambda_To_Time([LambdaSet], chopperObjcet.FlightPath)[0]) / 1e6) % 360
        chopperObjcet.phase = chopperObjcet.phase + PhaseAngle
        print 'Set ' + str(chopperObjcet.Name) + ' to ' + str(PhaseAngle) + ' degrees'


def calculate_transmitted_lambda2(Chopper_Obj=None, Number_of_Frames=None, timeAtChopper_from_lam=None,
                                         Lambda=None,
                                         histogram_in=None):
    Chopper_Times_min = []
    Chopper_Times_max = []
    Chopper_Times_min = np.array(Chopper_Obj.Chopper_Opening_Times)
    Chopper_Times_max = np.array(Chopper_Obj.Chopper_Closing_Times)
    FlightPath = Chopper_Obj.FlightPath

    single_frame_openings = len(Chopper_Times_min)
    print 'lambda array', Lambda.shape

    if Number_of_Frames > 1:
        for i in range(int(Number_of_Frames) - 1):
            Chopper_Times_min = np.append(Chopper_Times_min, [Chopper_Times_min[-single_frame_openings:] + 72000])
            Chopper_Times_max = np.append(Chopper_Times_max, [Chopper_Times_max[-single_frame_openings:] + 72000])

    print 'Chopper has ', len(Chopper_Times_min),' openings in ',Number_of_Frames,' frames'

    lambda_with_transmission = np.array([])
    histogram = np.array([])

    if len(timeAtChopper_from_lam.shape) > 1:
        histogram=evaluate_openings(timeAtChopper_from_lam,Chopper_Times_min, Chopper_Times_max)
        lambda_with_transmission=Lambda

    print timeAtChopper_from_lam.shape
    if len(timeAtChopper_from_lam.shape) == 1:
        lambda_with_transmission = Lambda
        histogram = np.zeros(histogram_in.shape)
        print lambda_with_transmission.shape,histogram.shape

        for j in range(len(Chopper_Times_min)):
            print '#### Opening ', j, '#######',Chopper_Obj.FlightPath,' m chopper #########'
            index2 = np.where(np.logical_and(timeAtChopper_from_lam > Chopper_Times_min[j],timeAtChopper_from_lam < Chopper_Times_max[j]))
            if len(index2[0]) > 0:
                histogram[index2]=histogram_in[index2]
            elif len(index2[0]) == 0:
                print 'zero trans'

    return lambda_with_transmission, histogram

def evaluate_openings(timeAtChopper_from_lam,Chopper_Times_min, Chopper_times_max):
    boolArray=np.full(timeAtChopper_from_lam.shape,dtype=bool,fill_value=False)

    for ct_min, ct_max in zip(Chopper_Times_min, Chopper_times_max):
        boolArray += (timeAtChopper_from_lam>ct_min)&(timeAtChopper_from_lam<ct_max)

    tmp = timeAtChopper_from_lam.astype(int)*boolArray.astype(int)
    tmp = tmp/tmp
    #tmp=np.nan_to_num(tmp)
    histo = np.sum(tmp,axis=0)
    return histo
