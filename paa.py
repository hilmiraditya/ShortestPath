import geocoder
from math import radians, cos, sin, asin, sqrt
from geopy.geocoders import Nominatim
from collections import defaultdict
from heapq import *

def currentlocation():
    g = geocoder.ip('me')
    cur_position = (g.latlng[0], g.latlng[1])
    return cur_position

def getlatlong(lokasi):
    geolocator = Nominatim()
    location = geolocator.geocode(lokasi)
    dest_position = (location.latitude, location.longitude)
    return dest_position

def getdistance(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2]) 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371
    return c * r

def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))
    q, seen, mins = [(0,f,())], set(), {f: 0}
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 in seen: continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))
    return float("inf")

if __name__ == "__main__":
    print "\n"
    print "Quiz 2 PAA F"
    print "======================================"
    print "Anggota : "
    print "5116100164 | Hilmi Raditya Prakoso"
    print "5116100151 | Falah Ath Thaariq Razzaq"
    print "5116100159 | Rahmad Yanuar Darmansyah"
    print "======================================"
    print "\n"

    nama_lokasi = list()
    distance = list()

    for a in range(0,7):
        temp = a+1
        input_nama_lokasi = raw_input("Masukkan nama lokasi ("+str(temp)+" dari 7) > ")
        nama_lokasi.append(input_nama_lokasi)

    print "\n"
    curlac = currentlocation()
    for a in range(0,7):
        print "lat dan long pada lokasi "+nama_lokasi[a]+" : "+str(getlatlong(nama_lokasi[a]))

    print "\n"
    print "harap menunggu, sedang membentuk graph !"
    edges = [
        (nama_lokasi[0], nama_lokasi[1], getdistance(getlatlong(nama_lokasi[0])[0],getlatlong(nama_lokasi[0])[1],getlatlong(nama_lokasi[1])[0],getlatlong(nama_lokasi[1])[1])),
        (nama_lokasi[0], nama_lokasi[3], getdistance(getlatlong(nama_lokasi[0])[0],getlatlong(nama_lokasi[0])[1],getlatlong(nama_lokasi[3])[0],getlatlong(nama_lokasi[3])[1])),
        (nama_lokasi[1], nama_lokasi[2], getdistance(getlatlong(nama_lokasi[1])[0],getlatlong(nama_lokasi[1])[1],getlatlong(nama_lokasi[2])[0],getlatlong(nama_lokasi[2])[1])),
        (nama_lokasi[1], nama_lokasi[3], getdistance(getlatlong(nama_lokasi[1])[0],getlatlong(nama_lokasi[1])[1],getlatlong(nama_lokasi[3])[0],getlatlong(nama_lokasi[3])[1])),
        (nama_lokasi[1], nama_lokasi[4], getdistance(getlatlong(nama_lokasi[1])[0],getlatlong(nama_lokasi[1])[1],getlatlong(nama_lokasi[4])[0],getlatlong(nama_lokasi[4])[1])),
        (nama_lokasi[2], nama_lokasi[4], getdistance(getlatlong(nama_lokasi[2])[0],getlatlong(nama_lokasi[2])[1],getlatlong(nama_lokasi[4])[0],getlatlong(nama_lokasi[4])[1])),
        (nama_lokasi[3], nama_lokasi[4], getdistance(getlatlong(nama_lokasi[3])[0],getlatlong(nama_lokasi[3])[1],getlatlong(nama_lokasi[4])[0],getlatlong(nama_lokasi[4])[1])),
        (nama_lokasi[3], nama_lokasi[5], getdistance(getlatlong(nama_lokasi[3])[0],getlatlong(nama_lokasi[3])[1],getlatlong(nama_lokasi[5])[0],getlatlong(nama_lokasi[5])[1])),
        (nama_lokasi[4], nama_lokasi[5], getdistance(getlatlong(nama_lokasi[4])[0],getlatlong(nama_lokasi[4])[1],getlatlong(nama_lokasi[5])[0],getlatlong(nama_lokasi[5])[1])),
        (nama_lokasi[4], nama_lokasi[6], getdistance(getlatlong(nama_lokasi[4])[0],getlatlong(nama_lokasi[4])[1],getlatlong(nama_lokasi[6])[0],getlatlong(nama_lokasi[6])[1])),        
        (nama_lokasi[5], nama_lokasi[6], getdistance(getlatlong(nama_lokasi[5])[0],getlatlong(nama_lokasi[5])[1],getlatlong(nama_lokasi[6])[0],getlatlong(nama_lokasi[6])[1])),        
    ]
    print "graph telah dibentuk !"
    print "\n"

    while True:
        print "List Lokasi yang telah diinput :"
        for a in range(0,7):
            nomor = a+1
            print str(nomor)+". "+nama_lokasi[a]
        pilihan_dari = input("Lokasi dari (masukkan nomor index) > ")
        pilihan_tujuan = input("Lokasi tujuan (masukkan nomor index) > ")
        print "\n"

        print "Hasil Pencarian Shortest-Path menggunakan Djikstra Algorithm :"
        print dijkstra(edges, nama_lokasi[pilihan_dari-1], nama_lokasi[pilihan_tujuan-1])
        print "\n"
