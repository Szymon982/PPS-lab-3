from thinkdsp import TriangleSignal, SquareSignal, SawtoothSignal
from thinkdsp import decorate
import numpy
import scipy
import matplotlib
from matplotlib import pyplot
import numpy as np


def zad1():
    print("zadanie1")
    signal = SquareSignal(1100)  # sygnał kwadratowy
    duration = signal.period * 8
    segment = signal.make_wave(duration, framerate=10000)  # biorę segment
    segment.plot(color="Red")
    decorate(xlabel='Czas (s)')
    pyplot.show()  # wyświetlam segment na wykresie
    print("\n")


def zad2():
    print("zadanie2")
    signal = TriangleSignal(440)  # sygnał trójkątny
    segment = signal.make_wave(0.01, framerate=10000)  # biorę segment
    segment.plot()
    decorate(xlabel='Czas (s)', ylabel='amplituda')
    pyplot.show()  # wyświetlam segment na wykresie

    spectrum = segment.make_spectrum()  # biorę widmo z segmentu i modyfikuję zgodnie z poleceniem zadania
    por1 = spectrum.hs[0]
    print("spectrum.hs[0] = ", por1)
    spectrum.hs[0] = 100
    print("dlugosc spectrum.hs[0] = ", len(spectrum.fs))

    por3 = spectrum.make_wave()  # konwertuję na falę aby wyświetlić na wykresie
    por3.plot()
    pyplot.show()
    print("\n")


def zad3(spectrum, sygnal):  # parametr sygnal dałem aby łatwo odróżnić który plik zawiera jaką falę
    spectrum.hs[0] = 0
    spectrum.fs = spectrum.fs[1:]  # usuwam zero z spectrum.fs
    for x in spectrum.hs:
        x = x / spectrum.fs
        print(x)
    spectrum.make_wave().write(sygnal + '-zad3_audio.wav')  # zapisuję do pliku


if __name__ == '__main__':
    zad1()  # uruchamiam zadanie 1

    zad2()  # uruchamiam zadanie 2

    print("\nzadanie 3")

    # tworzę sygnały do zadania nr 3

    signal1 = SquareSignal(500)  # kwadratowy
    wave1 = signal1.make_wave(duration=1, framerate=10000)
    segment1 = wave1.segment(duration=0.01)
    spectrum1 = segment1.make_spectrum()
    spectrum1.plot()
    pyplot.show()

    signal2 = TriangleSignal(500)  # trójkątny
    wave2 = signal2.make_wave(duration=1, framerate=10000)
    segment2 = wave2.segment(duration=0.015)
    spectrum2 = segment2.make_spectrum()
    spectrum2.plot()
    pyplot.show()

    signal3 = SawtoothSignal(500)  # pikokształtny
    wave3 = signal3.make_wave(duration=1, framerate=10000)
    segment3 = wave3.segment(duration=0.02)
    spectrum3 = segment3.make_spectrum()
    spectrum3.plot()
    pyplot.show()

    zad3(spectrum1, 'kwadratowy')

    zad3(spectrum2, 'trójkątny')

    zad3(spectrum3, 'pikokształtny')
