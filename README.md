# py_add_energy_groups
**This function adds energy groups to your mdp file**

I essentially just copied from [Alex K. Chew](https://www.alexkchew.com/tutorials/using-energy-groups-in-gromacs) but I dont know C so I uhh, just put it into python please dont hate me. He has a better and more thorough way of explaining this and has an actual job so maybe look at his tutorial okay?

* first: run your simulation
* make an index file that contains your energy groups of interest and nothing else
* upload your desired md.mdp file here and enter the energy_groups that you made in the index file
* make new tpr file _vide infra_
* `gmx grompp -f output_file.mdp -c confout.gro -p topol.top -o energy_groups.tpr -n energy_group_index.ndx`
* Re-run the sim using the -rerun flag _vide infra_
* `gmx mdrun -s penergy_groups.tpr -rerun existing_traj.trr  -e energy_groups.edr`
* Now use `gmx energy -f energy_groups.edr` to view your results
* LJ = lenny jones
* SR = short range
* Coul = you used PME so you cant decompose


Adopted from [Alex K. Chew](https://www.alexkchew.com/tutorials/using-energy-groups-in-gromacs)
