import main
import dataio
import out

out.Message("\t\t\t\t Source point :")

out.Head("\n\n\t\t\t\t *** Use Icp Algorithm For Moving image ***")
out.Error("\t\t\t\t\t\t\t\t\t!!!")
out.Warning("\t\t -- !!! For Use This Project First Convert Your *.nrrd File By Convert Method !!!")
out.Warning("\t\t -- !!! For Convert Your Image To *.nrrd Use MKConverter Project !!!")
out.Error("\t\t\t\t\t\t\t\t\t!!!")
out.Message("\t\t 1-Ready Data (Convert *.nrrd File To Usable Project Format)")
out.Message("\t\t 2-Start Operation")
out.MessageBlank("\t\t\t\t\t\t Select Your Operation : ")
inp = input("\t\t\t\t\t\t\t")
if inp == '1':
    out.MessageBlank("\t\t\t\t\t\t Enter Your Address File : ")
    address = input("\t\t\t\t\t\t\t")
    dataio.ConvertData(address)
elif inp == '2':
    # out.MessageBlank("\t\t\t\t\t\t Enter Your Address Folder Contain Input Files : ")
    # address = input("\t\t\t\t\t\t\t\t\t")
    main.Start('input/ready')
else:
    out.Error("\t\t\t\t\t\t[404] Operation Not Found")

#mk1m.txt mk1f.txt

#.split(':')[1]

#.strip()