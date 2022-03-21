miles1 = 1892
miles2 = 97
miles3 = 545
gallons1 = 71.4
gallons2 = 3.1
gallons3 = 30.8
totalmiles = miles1 + miles2 + miles3
totalgallons = gallons1 + gallons2 + gallons3

print(" Car1 %8d %8.1f %8.1f" % (miles1, gallons1, round(miles1/gallons1, 1)))
print(" Car2 %8d %8.1f %8.1f" % (miles2, gallons2, round(miles2/gallons2, 1)))
print(" Car3 %8d %8.1f %8.1f" % (miles3, gallons3, round(miles3/gallons3, 1)))
print(f" Car1 {miles1:8d} {gallons1:8.1f} {round((miles1/gallons1),1):8.1f}")
print(" Car2 {:8d} {:8.1f} {:8.1f}".format(miles2, gallons2, round(miles2/gallons2, 1)))
