#!/usr/bin/python
# __author__ = 'wenzhi'

import os
import time
from optparse import OptionParser
import csv
import pandas as pd
import re


def load_raw_data(file_name):
    data = {}
    # title = []
    with open(file_name, "r") as fp:
        for line in fp:
            if line != "":
                elements = line.strip().split()
                if line.startswith("#"):
                    # title = elements
                    pass
                else:
                    # print elements[1]
                    data[elements[0]] = elements
    print len(data), " total otus loaded"
    return data

def load_raw_data(file_name):
    data = {}
    # title = []
    with open(file_name, "r") as fp:
        for line in fp:
            if line != "":
                elements = line.strip().split()
                if line.startswith("#"):
                    # title = elements
                    pass
                else:
                    # print elements[1]
                    data[elements[0]] = elements
    print len(data), " total otus loaded"
    return data


def load_precal_files():
    global description
    global pathways
    global ko
    global all_meta_fun

    with open(description_file, "r") as fp:
        for line in fp:
            if line != "":
                description = line.split("\t")[1:]
                # print type(description)
    # print len(description)
    # print description

    with open(pathways_file, "r") as fp:
        for line in fp:
            if line != "":
                pathways = line.split("\t")[1:]
                # print type(pathways)
                # print len(pathways)
                # print pathways[4]

    with open(ko_file, "r") as fp:
        for line in fp:
            if line != "":
                ko = line.split("\t")[1:]
                # print "description", len(description)
                # print "pathways", len(pathways)
                # print "ko", len(ko)

    all_meta_fun = []
    with open(fun_file, "r") as fp:
        for line in fp:
            if line != "":
                all_meta_fun.append(line.strip().split("\t")[0])
                # print "description", len(description)
                # print "pathways", len(pathways)
                # print "ko", len(ko)
    # print all_meta_fun
    # print len(all_meta_fun)


def check_ko_num(lst):  # find all ko associated whit this otu
    index_lst = []
    for i in range(0, len(lst), 1):
        # print float(lst[i])
        if float(lst[i]) > 0:
            index_lst.append(i)
    # print index_lst
    # print len(index_lst), "the ko isnot zero"

    # metabo_index = []
    # for idx in index_lst:
    #     print idx
    #
    #     print pathways[4]
    #     print pathways[idx]
    # #     if "Metabolism" in description[idx]:
    # #         metabo_index.append(idx)
    # #
    # # print len(metabo_index), "metabo_index"

    return index_lst



def load_precal_files():
    global description
    global pathways
    global ko
    global all_meta_fun

    with open(description_file, "r") as fp:
        for line in fp:
            if line != "":
                description = line.split("\t")[1:]
                # print type(description)
    # print len(description)
    # print description


def check_ko_num(lst):  # find all ko associated whit this otu
    index_lst = []
    for i in range(0, len(lst), 1):
        # print float(lst[i])
        if float(lst[i]) > 0:
            index_lst.append(i)
    # print index_lst
    # print len(index_lst), "the ko isnot zero"

    # metabo_index = []
    # for idx in index_lst:
    #     print idx
    #
    #     print pathways[4]
    #     print pathways[idx]
    # #     if "Metabolism" in description[idx]:
    # #         metabo_index.append(idx)
    # #
    # # print len(metabo_index), "metabo_index"

    return index_lst



def load_precal_files():
    global description
    global pathways
    global ko
    global all_meta_fun

    with open(description_file, "r") as fp:
        for line in fp:
            if line != "":
                description = line.split("\t")[1:]
                # print type(description)
    # print len(description)
    # print description

def check_ko_num(lst):  # find all ko associated whit this otu
    index_lst = []
    for i in range(0, len(lst), 1):
        # print float(lst[i])
        if float(lst[i]) > 0:
            index_lst.append(i)
    # print index_lst
    # print len(index_lst), "the ko isnot zero"

    # metabo_index = []
    # for idx in index_lst:
    #     print idx
    #
    #     print pathways[4]
    #     print pathways[idx]
    # #     if "Metabolism" in description[idx]:
    # #         metabo_index.append(idx)
    # #
    # # print len(metabo_index), "metabo_index"

    return index_lst



def load_precal_files():
    global description
    global pathways
    global ko
    global all_meta_fun

    with open(description_file, "r") as fp:
        for line in fp:
            if line != "":
                description = line.split("\t")[1:]
                # print type(description)
    # print len(description)
    # print description

def check_ko_num(lst):  # find all ko associated whit this otu
    index_lst = []
    for i in range(0, len(lst), 1):
        # print float(lst[i])
        if float(lst[i]) > 0:
            index_lst.append(i)
    # print index_lst
    # print len(index_lst), "the ko isnot zero"

    # metabo_index = []
    # for idx in index_lst:
    #     print idx
    #
    #     print pathways[4]
    #     print pathways[idx]
    # #     if "Metabolism" in description[idx]:
    # #         metabo_index.append(idx)
    # #
    # # print len(metabo_index), "metabo_index"

    return index_lst



def load_precal_files():
    global description
    global pathways
    global ko
    global all_meta_fun

    with open(description_file, "r") as fp:
        for line in fp:
            if line != "":
                description = line.split("\t")[1:]
                # print type(description)
    # print len(description)
    # print description


    with open(pathways_file, "r") as fp:
        for line in fp:
            if line != "":
                pathways = line.split("\t")[1:]
                # print type(pathways)
                # print len(pathways)
                # print pathways[4]

    with open(ko_file, "r") as fp:
        for line in fp:
            if line != "":
                ko = line.split("\t")[1:]
                # print "description", len(description)
                # print "pathways", len(pathways)
                # print "ko", len(ko)

    all_meta_fun = []
    with open(fun_file, "r") as fp:
        for line in fp:
            if line != "":
                all_meta_fun.append(line.strip().split("\t")[0])
                # print "description", len(description)
                # print "pathways", len(pathways)
                # print "ko", len(ko)
    # print all_meta_fun
    # print len(all_meta_fun)


def check_ko_num(lst):  # find all ko associated whit this otu
    index_lst = []
    for i in range(0, len(lst), 1):
        # print float(lst[i])
        if float(lst[i]) > 0:
            index_lst.append(i)
    # print index_lst
    # print len(index_lst), "the ko isnot zero"

    # metabo_index = []
    # for idx in index_lst:
    #     print idx
    #
    #     print pathways[4]
    #     print pathways[idx]
    # #     if "Metabolism" in description[idx]:
    # #         metabo_index.append(idx)
    # #
    # # print len(metabo_index), "metabo_index"

    return index_lst


def list_the_function(lst):  # lst is index of ko
    # temp_fun_output = open('fun_output', 'w')

    # meta_fun_lst = []
    # for item in pathways:  # to test if the functions has duplicates
    #     if "Metabolism;Amino Acid Metabolism;Tyrosine metabolism" in item:
    #         # print >> temp_fun_output, item
    #         meta_fun_lst.append(item)
    # print len(set(meta_fun_lst)), "total meta fun # l3 set"
    # print len(meta_fun_lst), "total meta fun # l3"

    # print set(meta_fun_lst)

    metabolism_lst = []
    ko_lst = []
    fun_lst = []
    for i in lst:
        metabolism_lst.append(i)
        fun_lst.append(pathways[i])

            # print pathways[i]
    # print len(metabolism_lst), "total meta fun # l3"

    for k in metabolism_lst:
        ko_lst.append(ko[k])
    # print ko_lst
    # print fun_lst

    return len(metabolism_lst), ko_lst, fun_lst
    # print metabolism_lst

    # temp_fun_output.close()


def filter_otu_from_precal_file(d):
    global otu_with_ko_and_fun_dict
    otu_with_ko_and_fun_dict = {}
    # print d
    for key in d:
        # grep -P -w "\#OTU_IDs|95570"
        p = 'grep -P -w "\#OTU_IDs|' + key + '"' + " " + precalculated_file + " > temp"
        # print p
        os.system(p)

        with open("temp", "r") as fp:
            # ko_lst = []
            ko_num = []
            for line in fp:
                if line != "" and line.startswith(key):
                    elements = line.split("\t")[1:-1]
                    # print elements
                    for element in elements:
                        ko_num.append(element)

        # print key, "otu is "
        # print "ko_num", len(ko_num)
        # print ko_num
        os.remove("temp")
        index_lst = check_ko_num(ko_num)
        lenofmeta, ko_lst, fun_lst = list_the_function(index_lst)

        # if lenofmeta > 0:
        otu_with_ko_and_fun_dict[key] = [ko_lst]
        otu_with_ko_and_fun_dict[key].append(fun_lst)
    # print otu_with_ko_and_fun_dict
    print len(otu_with_ko_and_fun_dict), " otus have function"
    # return otu_with_ko_and_fun_dict


def load_mini_ref(d):
    global otu_with_ko_and_fun_dict
    otu_with_ko_and_fun_dict = {}
    mini_ref = {}
    ko_num = []

    with open("mini_ref", "r") as fp:
        for line in fp:
            if line != "":
                element = line.split("\t")
                mini_ref[element[0]] = element[1:]
    print "mini ref loaded"

    # with open("log", "w") as log:
    #     for ptw in all_meta_fun:  # bkup
    #         for key in d:
    #             # print key
    #             ko_num = mini_ref[key]
    #             index_lst = check_ko_num(ko_num)
    #             lenofmeta, ko_lst, fun_lst = list_the_function(index_lst)
    #
    #             if lenofmeta > 0:
    #                 otu_with_ko_and_fun_dict[key] = [ko_lst]
    #                 otu_with_ko_and_fun_dict[key].append(fun_lst)
    #         # print otu_with_ko_and_fun_dict
    #             print >> log, ptw, "|", len(otu_with_ko_and_fun_dict), "|otus have function"
    #             print otu_with_ko_and_fun_dict
    #         otu_with_ko_and_fun_dict = {}
    #         # return otu_with_ko_and_fun_dict
    # log.close()

    with open("log", "w") as log:
        for key in d:
            # print key
            ko_num = mini_ref[key]
            index_lst = check_ko_num(ko_num)
            lenofmeta, ko_lst, fun_lst = list_the_function(index_lst)

            if lenofmeta > 0:
                otu_with_ko_and_fun_dict[key] = [ko_lst]
                otu_with_ko_and_fun_dict[key].append(fun_lst)
        # print otu_with_ko_and_fun_dict
            #print >> log, ptw, "|", len(otu_with_ko_and_fun_dict), "|otus have function"
            print >> log, key, otu_with_ko_and_fun_dict[key][0], otu_with_ko_and_fun_dict[key][1]
        otu_with_ko_and_fun_dict = {}
        # return otu_with_ko_and_fun_dict
    log.close()

    # with open("log", "w") as log:
    #     for ptw in all_meta_fun:
    #         for key in d:
    #             # print key
    #             ko_num = mini_ref[key]
    #             index_lst = check_ko_num(ko_num)
    #             lenofmeta, ko_lst, fun_lst = list_the_function(index_lst, ptw)
    #
    #             if lenofmeta > 0:
    #                 otu_with_ko_and_fun_dict[key] = [ko_lst]
    #                 otu_with_ko_and_fun_dict[key].append(fun_lst)
    #
    #             print otu_with_ko_and_fun_dict[key][0]
    #             print otu_with_ko_and_fun_dict[key][1]
    #             print len(otu_with_ko_and_fun_dict[key][0])
    #             print len(otu_with_ko_and_fun_dict[key][1])
    #         # print otu_with_ko_and_fun_dict
    #         print >>log, ptw, "|", len(otu_with_ko_and_fun_dict), "|otus have function"
    #
    #
    #         # with open("otu_all_function", "w") as fp:
    #         #     for key in otu_with_ko_and_fun_dict:
    #         #         print >>fp, key, otu_with_ko_and_fun_dict[key][0], otu_with_ko_and_fun_dict[key][1],
    #         # fp.close()
    #
    #         otu_with_ko_and_fun_dict = {}
    #         # return otu_with_ko_and_fun_dict
    #
    #
    # log.close()


def lst2line(lst):  # list to line, split by \t
    line = ""
    for a in lst:
        if lst.index(a) != len(lst) - 1:
            line += a.strip() + ", "
        else:
            line += a.strip()
    return line


def lst2line_tab(lst):  # list to line, split by \t
    line = ""
    for a in lst:
        line += a.strip() + "\t"
    return line.strip()


def load_otu_table(fp, d):  # d is sample list
    otu_list = pd.read_csv(fp, sep="\t", skiprows=1, usecols=(['#OTU ID']))
    # print otu_list
    # print type(otu_list)
    t = otu_list['#OTU ID'].values.tolist
    # print t
    # with open(fp, 'r') as f:
    #     # f.readline().split() #  skip the "# Constructed from biom file"
    #     colnames = f.readline().split("\t")
    # print colnames
    # df = pd.read_csv(fp, sep="\t", usecols=(1, 2, 4))
    # df = pd.read_csv(fp, sep="\t", usecols=('#OTU ID', 'sample80', 'sample13'))
    # df = pd.read_csv(fp, sep="\t", names=colnames)
    # df = pd.read_csv(fp, sep="\t", names=['#OTU ID', 'sample80', 'sample13', 'sample14'])
    # df = pd.read_csv(fp, sep="\t", skiprows=1, usecols=('#OTU ID', 'sample80', 'sample13'))
    # saved_column = df.sample80

    # df = pd.read_csv(fp, sep="\t", skiprows=1)
    # print df
    # # print saved_column

    d_arrey = {}  # the data extracted from csv file
    otu_id = pd.read_csv(fp, sep="\t", skiprows=1, usecols=(['#OTU ID']))
    for k in d:
        col = natural_sort(d[k])
        # print col
        # print type(col)
        d_arrey[k] = pd.read_csv(fp, sep="\t", skiprows=1, usecols=(col))  # col is a list
        # print d_arrey['4w']
        # for key in natural_sort(d_arrey.keys()):
        #     print d_arrey[key]
        # print key
    # print d_arrey
    result = pd.concat([otu_id, d_arrey['4w'], d_arrey['8w'], d_arrey['12w'], d_arrey['16w']],
                       axis=1)  # combine the 4 dict/dataFrame
    # print result

    filename = "final_519_timeline.txt"
    if os.path.exists(filename):
        os.remove(filename)
    header = result.columns.values.tolist()
    # print header
    # print type(header)
    # print type(lst2line_tab(header))
    # print lst2line_tab(header)

    with open(filename, 'w') as fp:
        fp.write(lst2line_tab(header) + "\n")
    for otu in otu_with_ko_and_fun_dict:
        # print type(otu)
        row = result.loc[result['#OTU ID'] == int(otu)]
        row.to_csv(filename, sep='\t', index=False, header=False, mode='a')


def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)


def load_mapping_file(fp):  # return a sample list
    d = dict()
    items_sorted_d = dict()
    # with open(fp, 'r') as f:
    #     first_line = f.readline().split()
    # print first_line
    data = open(fp, "rb")
    csv_dict = csv.DictReader(data, delimiter="\t", quotechar="\"")
    for item in csv_dict:
        # print item
        # print item["Week"]
        if item[category] in d:
            d[item[category]].append(item["#SampleID"].strip())
        else:
            d[item[category]] = item["#SampleID"].strip().split()
    # print d
    # # print sorted(d.items())
    # for k in d:
    #     print natural_sort(d[k])
    #     items_sorted_d[k] = natural_sort(d[k])
    # # print items_sorted_d
    # return items_sorted_d
    return d


def get_args():
    desc = "load OTU data"
    usage = "KEGG_KO.py -i OTUs_list -t OTUs_table -m mapping_file -c category"
    #  python KEGG_KO.py -i otu_table.csv.sorted -t otu_table.csv.sorted -m combined_mapping_file.txt -c Week
    parser = OptionParser(usage=usage, description=desc)
    parser.add_option("-i", "--OTUs_list", type="string", dest="OTUs_list", help="Input File Name", default="null")
    parser.add_option("-t", "--OTUs_table", type="string", dest="OTUs_table", help="Input File Name", default="null")
    parser.add_option("-m", "--mapping_file", type="string", dest="mapping_file", help="Input File Name",
                      default="null")
    parser.add_option("-c", "--category", type="string", dest="category", help="category", default="null")
    (options, args) = parser.parse_args()
    if options.OTUs_list == "null":
        print "parameters missing..."
        print usage
        sys.exit(1)
    return options


def main():
    starttime = time.time()

    # link the otus and KO start
    load_precal_files()
    OTUs_list_file = load_raw_data(options.OTUs_list)
    # print OTUs_list_file
    # otu_with_ko_and_fun_dict = filter_otu_from_precal_file(OTUs_list_file)
    load_mini_ref(OTUs_list_file)
    # link the otus and KO end

    # process the otu table start

    category_d = load_mapping_file(options.mapping_file)
    load_otu_table(options.OTUs_table, category_d)
    # process the otu table end

    print "run time is :", round((time.time() - starttime), 6), "s"


def main_new():
    starttime = time.time()

    # link the otus and KO start
    load_precal_files()
    OTUs_list_file = load_raw_data(options.OTUs_list)
    # print OTUs_list_file
    # otu_with_ko_and_fun_dict = filter_otu_from_precal_file(OTUs_list_file)
    load_mini_ref(OTUs_list_file)
    # link the otus and KO end

    # process the otu table start

    category_d = load_mapping_file(options.mapping_file)
    load_otu_table(options.OTUs_table, category_d)
    # process the otu table end

    print "run time is :", round((time.time() - starttime), 6), "s"


if __name__ == '__main__':
    options = get_args()
    current_path = os.getcwd()
    # define
    precalculated_file = "ko_13_5_precalculated.tab"
    description_file = "metadata_KEGG_Description"
    pathways_file = "metadata_KEGG_Pathways"
    ko_file = "ko"
    fun_file = "meta_ref_all_fun"
    # fun_file = "meta_ref"
    # description = []
    # pathways = []
    # ko = []
    category = options.category

    main()
