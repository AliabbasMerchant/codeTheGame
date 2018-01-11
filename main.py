"""Run the main.py module separately for each file, by commenting out the other file names.
After running it for each and every file, comment out the 'inn' parts.Uncomment the part after 'FINAL' and run it"""
import inning
import consolidate
import dream11

# """This portion has been commented out as there is a problem of data duplication which occurs when employing this method."""
# file_list = []
# inn = {}
# for i in range(1,11) :
#     inn[i] = inning.Inning()
#     inn[i].read_csv("outputf" + str(i) + "1st.csv")
#     inn[i].allot_data()
#     inn[i].calculate_scores()
#     file_list.append(inn[i].save_to_json())
#     if i == 1:
#         inn[12] = inning.Inning()
#         inn[12] = inning.Inning()
#         inn[12].read_csv("outputf" + str(i) + "2nd.csv")
#         inn[12].allot_data()
#         inn[12].calculate_scores()
#         file_list.append(inn[12].save_to_json())
#     if i == 2:
#         inn[22] = inning.Inning()
#         inn[22] = inning.Inning()
#         inn[22].read_csv("outputf" + str(i) + "2nd.csv")
#         inn[22].allot_data()
#         inn[22].calculate_scores()
#         file_list.append(inn[22].save_to_json())
# consolidate = consolidate.Consolidate()
# consolidate.consolidate(file_list)
# consolidate.save_to_json()
#
# Dream11 = dream11.dream11()
# Dream11.read()
# Dream11.save_to_json()


inn = inning.Inning()
# uncomment the file which is required to be processed at the current run
# inn.read_csv("outputf11st.csv")
# inn.read_csv("outputf12nd.csv")
# inn.read_csv("outputf21st.csv")
# inn.read_csv("outputf22nd.csv")
# inn.read_csv("outputf31st.csv")
# inn.read_csv("outputf41st.csv")
# inn.read_csv("outputf51st.csv")
# inn.read_csv("outputf61st.csv")
# inn.read_csv("outputf71st.csv")
# inn.read_csv("outputf81st.csv")
# inn.read_csv("outputf91st.csv")
# inn.read_csv("outputf101st.csv")
inn.allot_data()
inn.calculate_scores()
inn.save_to_json()

# FINAL:
# file_list = ["DD vs RPS_data.json",
#              "GL vs KKR_data.json",
#              "GL vs SRH_data.json",
#              "KKR vs MI_data.json",
#              "MI vs RPS_data.json",
#              "RCB vs DD_data.json",
#              "RCB vs KXIP_data.json",
#              "RCB vs SRH_data.json",
#              "RPS vs KXIP_data.json",
#              "RPS vs MI_data.json",
#              "SRH vs MI_data.json",
#              "SRH vs RCB_data.json",
#              ]
# consolidate = consolidate.Consolidate()
# consolidate.consolidate(file_list)
# consolidate.save_to_json()
#
# Dream11 = dream11.dream11()
# Dream11.read()
# Dream11.save_to_json()
#
# print("DONE!!!")