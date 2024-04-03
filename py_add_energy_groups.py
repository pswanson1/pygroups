import shutil
def py_add_energy_groups(input_mdp_file,output_mdp_file,energy_groups):
    # Adopted from [Alex K. Chew](https://www.alexkchew.com/tutorials/using-energy-groups-in-gromacs)
    # i just rewrote his stuff in python because i dont know any real languages 
    # function takes input .mdp file, copies it and appends your desired energy groups, then spits it out as the output_mdp_file
    # make sure your inputs are strings 
    #
    # Overview of what you are doing
    #
    # * first: run your simulation    
    # * make an index file that contains your energy groups of interest and nothing else
    # * upload your desired md.mdp file here and enter the energy_groups that you made in the index file in the form: "group1 group2 groupN"
    # * make new tpr file _vide infra_
    # * `gmx grompp -f output_file.mdp -c confout.gro -p topol.top -o energy_groups.tpr -n energy_group_index.ndx`
    # * Re-run the sim using the -rerun flag _vide infra_
    # * `gmx mdrun -s penergy_groups.tpr -rerun existing_traj.trr  -e energy_groups.edr`
    # * Now use `gmx energy -f energy_groups.edr` to view your results

    if type(input_mdp_file) != str:
      raise ValueError("Your input {} Should be a string".format(input_mdp_file))
    elif type(energy_groups) != str:
      raise ValueError("Your input {} Should be a string".format(energy_groups))
    else:
      shutil.copyfile(input_mdp_file, output_mdp_file)

      with open(output_mdp_file, 'a') as file: # open and append to the input_mdp
          file.write("\n")
          file.write("; ENERGY GROUPS\n")
          file.write("energygrps = {}\n".format(energy_groups))

      print("----- mdp_add_energy_groups -----")
      print("--> Created {} from {}".format(output_mdp_file, input_mdp_file))
      print("--> Added energy groups: {}".format(energy_groups))
