import xml.etree.ElementTree as xml
import datetime

f1name = "./segments"
f2name = "./text"
def open_transcript1(f1name):
    with open(f1name, "r") as f1:
        transcript1 = f1.read()
    return (transcript1)

def clean_transcript1(transcript1):
    if " ;" in transcript1:
        transcript1 = transcript1.replace(" ;", "\n")
        transcript1 = transcript1.split("\n\n")
    return(transcript1)

def transcript1_seprate(transcript1):
    transcript1 = transcript1.split("\n")
    return(transcript1)


def time_split(segment1):
    segment1 = segment1.split(".0 ")
    return(segment1)

def file_name(name1):
        segment1name = name1.split("0000 ")[1]
        segment1name = segment1name.split(" 0")
        segment1name = segment1name[0]
        return(segment1name)

def id1_split(idname):
    idname = idname.split(" ")
    return(idname)

# for filename and time stamp 

transcript1 = open_transcript1(f1name)
transcript1 = clean_transcript1(transcript1)
segment1 = transcript1_seprate(transcript1[0])
# time1 = time_split(segment1[0])
time2 = time_split(segment1[0])
idname1 = id1_split(segment1[0])
name1 = file_name(time2[0])

def open_transcript2(f2name):
    with open(f2name, encoding="utf8") as f2:
        transcript2 = f2.read()
    return (transcript2)

def clean_transcript2(transcript2):
    if " ;" in transcript2:
        transcript2 = transcript2.replace(" ;", "\n")
        transcript2 = transcript2.split("\n\n")
    return(transcript2)

def transcript2_seprate(transcript2):
    transcript2 = transcript2.split("\n")
    return(transcript2)

def id2_split(idname):
    idname = idname.split(" ")
    return(idname)

transcript2 = open_transcript2(f2name)
transcript2 = clean_transcript2(transcript2)
segment2 = transcript2_seprate(transcript2[0])
idname2 = id2_split(segment2[0])
# print((segment2[1]).encode('utf8'))
# print(idname2[1])


# create xml file
def create_xml(xmlfile):
    
    # tree = xml.ElementTree(root)
    with open(xmlfile, "w", encoding="utf-8") as f:
        
        for data in transcript1:
            if search == data:
                f.write("<?xml version='1.0' encoding='UTF-8'?>\n")
                f.write("<transcript lang='hindi'>\n")
                # f.write("<line timestamp='0.0' speaker='speaker_1'>\n")
                # f.write("<word timestamp='0.0' is_valid='true'>\n")
                # f.write("</line>\n")
                seg = transcript1_seprate(data)
                for i in seg:
                    b = []
                    time = time_split(i)
                    try:
                        time = time[1]
                        time = int(float(time))
                        time = str(datetime.timedelta(seconds = time))
                        b.append(time)
                    except IndexError:
                        pass
                    f.write(f"<line timestamp='{time}' speaker='speaker_1'> \n")
                    te = id1_split(i)
                    te = te[0]
                    for data1 in transcript2:
                        seg1 = transcript2_seprate(data1)
                        for j in seg1:
                            te1 = id2_split(j)
                            te2 = te1[0]
                            word = (te1[1:])
                            if te == te2:
                                for k in word:
                                    k = k.encode('utf-8')
                                    k = k.decode()
                                    f.write(f"<word timestamp=''>{k} </word>\n")
                            
                    f.write("</line>\n")
                f.write("</transcript>")


for data in transcript1:
    search = data
    segmentq = transcript1_seprate(data)
    timeq = time_split(segmentq[0])
    nameq = file_name(timeq[0])
    create_xml(nameq + ".xml")
    
            