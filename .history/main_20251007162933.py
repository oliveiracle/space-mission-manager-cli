
import missions

missions.show_title()
print("Choose a mission to learn more about:")
print("1-Perseverance | 2-James Webb | 3-Voyager 1 | 4-Hubble | 5-Curiosity")
print("6-Spitzer | 7-Cassini-Huygens | 8-New Horizons | 9-Galileo | 10-Kepler")
print("11-Chandra | 12-Juno | 13-TESS | 14-OSIRIS-REx | 15-Dawn")
print("16-SpaceX Starship | 17-Blue Origin | 18-Ariane 5 | 19-Soyuz")
print("20-Falcon 9 | 21-Atlas V | 22-Delta IV | 23-SLS")
print("24-Crew Dragon | 25-Starlink")

option = input("Enter your choice (1-25): ")
if option == "1":
    # Mission details com f-strings
    # Perseverance details
    mission_name = "Perseverance"
    mission_type = "Mars Rover"
    planet = "Mars"
    purpose = "search for signs of past life"
    builder = "NASA's Jet Propulsion Laboratory"
    launch_year = 2020
    landing_year = 2021
    cost = 2_700_000_000  # 2.7 billion USD
    
    print(missions.mission1)
    print(f"🔴 {mission_type}: {mission_name}")
    print(f"📍 Destination: {planet}")
    print(f"🎯 Primary Mission: To {purpose} and analyze Martian geology")
    print(f"🚀 Launched: {launch_year} | 🛬 Landed: {landing_year}")
    print(f"💰 Mission Cost: ${cost:,} USD")
    print(f"🏭 Built by: {builder}")
    print(f"🌟 Exploring God's magnificent creation on {planet} since {landing_year}!")
    
elif option == "2":
    # James Webb details
    mission_name = "James Webb Space Telescope"
    mission_type = "Space Telescope"
    specialty = "infrared observations"
    partners = "NASA, ESA, and CSA"
    launch_year = 2021
    orbit_location = "L2 Lagrange Point"
    mirror_size = 6.5  # meters
    cost = 10_000_000_000  # 10 billion USD
    
    print(missions.mission2)
    print(f"🔭 {mission_type}: {mission_name}")
    print(f"🌌 Speciality: Advanced {specialty}")
    print(f"🪞 Primary Mirror: {mirror_size}m diameter")
    print(f"📍 Operating Location: {orbit_location}")
    print(f"🚀 Launched: {launch_year}")
    print(f"💰 Total Cost: ${cost:,} USD")
    print(f"🤝 International Partnership: {partners}")
    print(f"✨ Revealing the wonders of God's universe since {launch_year}!")
    
elif option == "3":
    # Voyager 1 details
    mission_name = "Voyager 1"
    mission_type = "Space Probe"
    specialty = "interstellar exploration"
    partners = "NASA"
    launch_year = 1977
    orbit_location = "Interstellar Space"
    cost = 250_000_000  # 250 million USD
    
    print(missions.mission3)
    print(f"🚀 {mission_type}: {mission_name}")
    print(f"🌌 Specialty: {specialty}")
    print(f"📍 Current Location: {orbit_location}")
    print(f"🚀 Launched: {launch_year}")
    print(f"💰 Mission Cost: ${cost:,} USD")
    print(f"🤝 Built by: {partners}")
    print(f"✨ Exploring the vastness of God's universe since {launch_year}!")
    print("description: A space probe that has traveled beyond our")
    print("solar system, providing valuable data about interstellar space.")
    print("It is the farthest human-made object from Earth,")
    print("continuing to send data back to NASA as it journeys through the")
    print("interstellar medium.")
    print("Launched in 1977, it has provided invaluable insights into")
    print("the outer planets and the heliosphere.")
    print("and was built by NASA.")
    
elif option == "4":
    # Hubble details
    mission_name = "Hubble Space Telescope"
    mission_type = "Space Telescope"
    specialty = "high-resolution imaging"
    partners = "NASA and ESA"
    launch_year = 1990      
    orbit_location = "Low Earth Orbit"
    cost = 10_000_000_000  # 10 billion USD 
    service_missions = 5    
    
    print(missions.mission4)
    print(f"🔭 {mission_type}: {mission_name}")
    print(f"🌌 Specialty: {specialty}") 
    print(f"📍 Operating Location: {orbit_location}"
    print(f"🚀 Launched: {launch_year}")
    print(f"💰 Total Cost: ${cost:,} USD")
    print(f"🛠️ Service Missions: {service_missions}")
    print(f"🤝 International Partnership: {partners}")
    print(f"✨ Unveiling the beauty of God's universe since {launch_year}!")
    print(f"🏭 Built by: {partners}")
   
elif option == "5":
    # Curiosity details
    mission_name = "Curiosity"
    mission_type = "Mars Rover"
    planet = "Mars"
    purpose = "analyze soil and rock samples"
    builder = "NASA's Jet Propulsion Laboratory"    
    launch_year = 2011      
    landing_year = 2012
    cost = 2_500_000_000  # 2.5 billion USD

    print(missions.mission5)
    print(f"🔴 {mission_type}: {mission_name}"
    print(f"📍 Destination: {planet}")
    print(f"🎯 Primary Mission: To {purpose} to understand Mars' geology and climate")
    print(f"🚀 Launched: {launch_year} | 🛬 Landed
    print(f"💰 Mission Cost: ${cost:,} USD")
    print(f"🏭 Built by: {builder}")
    print(f"🌟 Exploring God's magnificent creation on {planet} since {landing_year}
    
    
elif option == "6":
# Spitzer details
    mission_name = "Spitzer Space Telescope"    
    mission_type = "Space Telescope"
    specialty = "infrared observations" 
    partners = "NASA and JPL"
    launch_year = 2003
    orbit_location = "Heliocentric Orbit"
    mirror_size = 0.85  # meters
    cost = 720_000_000  # 720 million USD
    
    print(missions.mission6)
    print(f"🔭 {mission_type}: {mission_name}")
    print(f"🌌 Specialty: Advanced {specialty}")
    print(f"🪞 Primary Mirror: {mirror_size}m diameter")
    print(f"📍 Operating Location: {orbit_location}")
    print(f"🚀 Launched: {launch_year}")
    print(f"💰 Total Cost: ${cost:,} USD")
    print(f"🤝 Built by: {partners}")
    print(f"✨ Revealing the wonders of God's universe since {launch_year}!")

    
elif option == "7":
# Cassini-Huygens details
    mission_name = "Cassini-Huygens"
    mission_type = "Orbiter and Lander"
    planet = "Saturn"       
    purpose = "study Saturn and its moons"
    builder = "NASA and Italy's ASI"
    launch_year = 1997
    arrival_year = 2004
    end_year = 2017
    cost = 3_900_000_000  # 3.9 billion USD 
    
    print(missions.mission7)
    print(f"🪐 {mission_type}: {mission_name}")
    print(f"📍 Destination: {planet}")
    print(f"🎯 Primary Mission: To {purpose}  analyze Saturn's rings.")
    print(f"🚀 Launched: {launch_year} | 🛬 Arrived: {arrival_year} | Ended: {end_year}")   
    print(f"💰 Mission Cost: ${cost:,} USD")
    print(f"🏭 Built by: {builder}")
    print(f"🌟 Exploring God's magnificent creation on {planet} from {arrival_year}
    print(f" to {end_year}!")
    
    
elif option == "8":
# New Horizons details
    mission_name = "New Horizons"
    mission_type = "Space Probe"
    planet = "Pluto and Kuiper Belt"
    purpose = "conduct a flyby of Pluto and study Kuiper Belt objects"
    builder = "Johns Hopkins University Applied Physics Laboratory"
    launch_year = 2006
    arrival_year = 2015
    cost = 700_000_000  # 700 million USD
    
    print(missions.mission8)
    print(f"🚀 {mission_type}: {mission_name}")
    print(f"📍 Destination: {planet}")
    print(f"🎯 Primary Mission: To {purpose} and gather data on these distant objects")
    print(f"🚀 Launched: {launch_year} | 🛬 Arrived
    print(f"💰 Mission Cost: ${cost:,} USD")
    print(f"🏭 Built by: {builder}")
    print(f"🌟 Exploring God's magnificent creation in the outer solar system since {arrival_year}")
    
    
elif option == "9":
# Galileo details
    mission_name = "Galileo"
    mission_type = "Orbiter and Probe"
    planet = "Jupiter"      
    purpose = "study Jupiter and its moons"
    builder = "NASA's Jet Propulsion Laboratory"
    launch_year = 1989
    arrival_year = 1995
    end_year = 2003
    cost = 1_600_000_000  # 1.6 billion USD
    
    print(missions.mission9)
    print(f"🪐 {mission_type}: {mission_name}")
    print(f"📍 Destination: {planet}")
    print(f"🎯 Primary Mission: To {purpose} and analyze its atmosphere and magnetosphere")
    print(f"🚀 Launched: {launch_year} | 🛬 Arrived: {arrival_year} | Ended: {end_year}")
    print(f"💰 Mission Cost: ${cost:,} USD")
    print(f"🏭 Built by: {builder}")
    print(f"🌟 Exploring God's magnificent creation on {planet} from {arrival_year} to {end_year}!")
    
elif option == "10":
# Kepler details    
    mission_name = "Kepler Space Telescope"
    mission_type = "Space Telescope"        
    specialty = "exoplanet discovery"
    partners = "NASA and JPL"           
    launch_year = 2009
    end_year = 2018
    mirror_size = 0.95  # meters    
    cost = 600_000_000  # 600 million USD   
      
    print(missions.mission10)
    print(f"🔭 {mission_type}: {mission_name}")
    print(f"🌌 Specialty: {specialty}")
    print(f"🪞 Primary Mirror: {mirror_size}m diameter")
    print(f"📍 Operating Location: Earth-trailing heliocentric orbit")
    print(f"🚀 Launched: {launch_year} | Ended: {end_year}")
    print(f"💰 Total Cost: ${cost:,} USD")
    print(f"🤝 Built by: {partners}"
    print(f"✨ Discovering new worlds in God's universe from {launch_year} to {end_year}!")
    

elif option == "11":
# Chandra details   
    mission_name = "Chandra X-ray Observatory"
    mission_type = "Space Telescope"
    specialty = "X-ray observations"
    partners = "NASA and Smithsonian Astrophysical Observatory"
    launch_year = 1999
    orbit_location = "High Earth Orbit"
    mirror_size = 1.2  # meters     
    cost = 1_600_000_000  # 1.6 billion USD

    print(missions.mission11)
    print(f"🔭 {mission_type}: {mission_name}")
    print(f"🌌 Specialty: Advanced {specialty}")
    print(f"🪞 Primary Mirror: {mirror_size}m diameter")
    print(f"📍 Operating Location: {orbit_location}")
    print(f"🚀 Launched: {launch_year}")
    print(f"💰 Total Cost: ${cost:,} USD")
    print(f"🤝 Built by: {partners}")
    print(f"✨ Revealing the high-energy universe of God's creation since {launch_year}!")

elif option == "12
# Juno details
    mission_name = "Juno"
    mission_type = "Orbiter"
    planet = "Jupiter"
    purpose = "study Jupiter's atmosphere, magnetic field, and internal structure"
    builder = "Lockheed Martin"
    launch_year = 2011      
    arrival_year = 2016     
    cost = 1_100_000_000  # 1.1 billion USD 
    
    print(missions.mission12)
    print(f"🪐 {mission_type}: {mission_name}")
    print(missions.mission12)
    print(f"📍 Destination: {planet}")
    print(f"🎯 Primary Mission: To {purpose} and understand its formation and evolution")
    print(f"🚀 Launched: {launch_year} | 🛬 Arrived: {arrival_year}")
    print(f"💰 Mission Cost: ${cost:,} USD")
    print(f"🏭 Built by: {builder}"
    print(f"🌟 Exploring God's magnificent creation on {planet} since {arrival_year}!")
    
    
elif option == "13"
# TESS details  
    mission_name = "Transiting Exoplanet Survey Satellite (TESS)"
    mission_type = "Space Telescope"
    speciality = "exoplanet discovery"
    partners = "NASA and MIT"
    launch_year = 2018
    orbit_location = "High Earth Orbit"
    mirror_size = 0.1  # meters
    cost = 337_000_000  # 337 million USD   
    
    print(missions.mission13)
    print(f"🔭 {mission_type}: {mission_name}")
    print(f"🌌 Speciality: {speciality}")
    print(f"🪞 Primary Mirror: {mirror_size}m diameter")
    print(f"📍 Operating Location: {orbit_location}")
    print(f"🚀 Launched: {launch_year}")
    print(f"💰 Total Cost: ${cost:,} USD")
    print(f"🤝 Built by: {partners}")
    print(f"✨ Discovering new worlds in God's universe since {launch_year}!")
    
elif option == "14":
    print(missions.mission14)
    print("description: A mission that collected samples from the")
    print("asteroid Bennu and is returning them to Earth for analysis.")
    print("It successfully collected pristine samples that may contain")
    print("clues about the early solar system and origins of life.")
    print("Was built by Lockheed Martin for NASA.")
elif option == "15":
    print(missions.mission15)
    print("description: A mission that studied the two largest objects")
    print("in the asteroid belt, Vesta and Ceres.")
    print("It provided detailed maps and composition data")
    print("of these ancient remnants from the early solar system.")
    print("Was built by Orbital ATK for NASA.")
elif option == "16":
    print(missions.mission16)
    print("description: A spacecraft designed for interplanetary travel,")
    print("with the goal of enabling human missions to Mars and beyond.")
    print("It's designed to be fully reusable and carry large crews")
    print("and cargo to the Moon, Mars, and other destinations.")
    print("Was built by SpaceX.")
elif option == "17":
    print(missions.mission17)
    print("description: A suborbital spaceflight vehicle designed")
    print("to take passengers to the edge of space.")
    print("It offers commercial space tourism flights")
    print("providing a few minutes of weightlessness.")
    print("Was built by Blue Origin.")
elif option == "18":
    print(missions.mission18)
    print("description: A heavy-lift launch vehicle used to")
    print("deliver payloads to orbit.")
    print("It has been one of the most reliable launch vehicles")
    print("for commercial and scientific satellites.")
    print("Was built by Arianespace and ESA.")
elif option == "19":
    print(missions.mission19)
    print("description: A spacecraft used for human spaceflight")
    print("missions to the International Space Station and other")
    print("destinations.")
    print("It has been the most reliable human spaceflight system")
    print("with over 140 crewed missions.")
    print("Was built by Roscosmos (Russia).")
elif option == "20":
    print(missions.mission20)
    print("description: A reusable rocket designed to deliver payloads")
    print("to orbit and return to Earth for refurbishment and reuse.")
    print("It revolutionized the space industry by making")
    print("launches more cost-effective through reusability.")
    print("Was built by SpaceX.")
elif option == "21":
    print(missions.mission21)
    print("description: A versatile launch vehicle used to deliver")
    print("payloads to a variety of orbits.")
    print("It has launched many important NASA missions")
    print("including Mars rovers and space telescopes.")
    print("Was built by United Launch Alliance (ULA).")
elif option == "22":
    print(missions.mission22)
    print("description: A heavy-lift launch vehicle used to deliver")
    print("large payloads to orbit.")
    print("It specializes in launching large government")
    print("and military satellites to high orbits.")
    print("Was built by United Launch Alliance (ULA).")
elif option == "23":
    print(missions.mission23)
    print("description: A next-generation launch vehicle designed")
    print("for deep space exploration missions.")
    print("It's designed to launch Artemis missions")
    print("and send humans back to the Moon.")
    print("Was built by NASA and Boeing.")
elif option == "24":
    print(missions.mission24)
    print("description: A spacecraft designed for human spaceflight")
    print("missions to the International Space Station and beyond.")
    print("It restored America's capability to launch astronauts")
    print("from US soil after the Space Shuttle retirement.")
    print("Was built by SpaceX.")
elif option == "25":
    print(missions.mission25)
    print("description: A satellite constellation designed to provide")
    print("global internet coverage.")
    print("It aims to provide high-speed internet access")
    print("to underserved and remote areas worldwide.")
    print("Was built by SpaceX.")
else:
    print("Invalid option. Please select a number between 1 and 25.")
    raise SystemExit()

