import matplotlib.pyplot as plt

# Initial conditions (Balanced State)
nutrients = 30
algae = 10
zooplankton = 5
detritus = 5  # Dead organic matter

# Simulation parameters
time_steps = 300
nutrient_input_rate = 0.2
algae_growth_rate = 0.05
zooplankton_grazing_rate = 0.011

algae_death_rate = 0.01
detritus_decomposition_rate = 0.01
nutrient_uptake_rate = 0.02
zooplankton_death_rate = 0.01

# Lists for plotting
nutrients_history = [nutrients]
algae_history = [algae]
zooplankton_history = [zooplankton]
detritus_history = [detritus]

# Simulation loop
for t in range(time_steps):
    # Balanced State Dynamics
    algae_growth = algae * algae_growth_rate * (nutrients / 100)
    algae_loss_grazing = algae * zooplankton_grazing_rate * (zooplankton / 100)
    algae_loss_death = algae * algae_death_rate
    algae += algae_growth - algae_loss_grazing - algae_loss_death

    zooplankton_growth = zooplankton * zooplankton_grazing_rate * (algae / 100)
    zooplankton_loss = zooplankton * zooplankton_death_rate * 1/(algae+0.01)
    zooplankton += zooplankton_growth - zooplankton_loss

    nutrients_uptake = algae * nutrient_uptake_rate
    detritus_decomposition = detritus * detritus_decomposition_rate
    nutrients += detritus_decomposition - nutrients_uptake + nutrient_input_rate

    detritus += algae_loss_death + zooplankton_loss - detritus_decomposition

    # Eutrophication Trigger (Increased Nutrient Input)
    if t == 50:
        nutrient_input_rate = 10  # Significantly increase input
    if t == 75:
        nutrient_input_rate = -1 # try to revert it back

    # Eutrophication Dynamics (Positive Feedback & Shift)
    if nutrients > 90:
        algae_growth *= 1.005  # Increased growth rate

    #no negative values
    [nutrients, algae, zooplankton, detritus] = [max(0, var) for var in [nutrients, algae, zooplankton, detritus]]
    
    nutrients_history.append(nutrients)
    algae_history.append(algae)
    zooplankton_history.append(zooplankton)
    detritus_history.append(detritus)

# Plotting
plt.figure(figsize=(14, 8))
plt.plot(nutrients_history, label="Nutrients")
plt.plot(algae_history, label="Algae")
#plt.plot(oxygen_history, label="Oxygen")
plt.plot(zooplankton_history, label="Zooplankton")
plt.plot(detritus_history, label="Detritus")
plt.xlabel("Time Steps")
plt.ylabel("Level")
plt.title("Eutrophication Model: Balanced State & Irreversible Shift")
plt.legend()
plt.grid(True)
plt.show()
