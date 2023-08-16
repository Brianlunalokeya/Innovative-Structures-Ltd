from app import db, Client, Project, TeamMember, Service

# Create sample data for Clients
clients_data = [
    {"name": "ABC Construction", "email": "info@abcconstruction.com"},
    {"name": "Elegant Designs Ltd", "email": "contact@elegantdesigns.com"},
    {"name": "Global Builders", "email": "info@globalbuilders.com"},
    {"name": "City Engineering", "email": "contact@cityengineering.com"},
    {"name": "Skyline Architects", "email": "info@skylinearchitects.com"},
    {"name": "Urban Developments", "email": "contact@urbandevelopments.com"},
    {"name": "Mega Builders", "email": "info@megabuilders.com"},
    {"name": "Innovative Structures", "email": "contact@innovativestructures.com"},
    {"name": "Steadfast Constructions", "email": "info@steadfastconstructions.com"},
    {"name": "Modern Designs", "email": "contact@moderndesigns.com"},
]

for client_data in clients_data:
    client = Client(**client_data)
    db.session.add(client)

# Create sample data for Projects
projects_data = [
    {"title": "Skyscraper Tower", "description": "Design and construction of a 50-story skyscraper."},
    {"title": "Renovation of Heritage Building", "description": "Historical building restoration project."},
    {"title": "Bridge Overpass", "description": "Engineering of a new overpass for improved traffic flow."},
    {"title": "Residential Complex", "description": "Development of a modern housing complex."},
    {"title": "Commercial Plaza", "description": "Construction of a bustling commercial center."},
    {"title": "Hospital Expansion", "description": "Expansion of a healthcare facility for better services."},
    {"title": "Sports Stadium", "description": "Design and construction of a sports arena."},
    {"title": "Highway Construction", "description": "New highway construction for enhanced connectivity."},
    {"title": "Educational Campus", "description": "Campus construction for an educational institution."},
    {"title": "Mixed-Use Development", "description": "Integrated development with residential, commercial, and recreational spaces."},
]

for project_data in projects_data:
    project = Project(**project_data)
    db.session.add(project)

# Create sample data for Team Members
team_members_data = [
    {"name": "John Smith", "position": "Project Manager"},
    {"name": "Emily Johnson", "position": "Architect"},
    {"name": "Daniel Brown", "position": "Civil Engineer"},
    {"name": "Sophia Clark", "position": "Structural Engineer"},
    {"name": "Michael Lee", "position": "Electrical Engineer"},
    {"name": "Olivia Taylor", "position": "Surveyor"},
    {"name": "William Miller", "position": "Construction Manager"},
    {"name": "Ava Martinez", "position": "Interior Designer"},
    {"name": "James Anderson", "position": "Mechanical Engineer"},
    {"name": "Emma Turner", "position": "Urban Planner"},
]

for member_data in team_members_data:
    member = TeamMember(**member_data)
    db.session.add(member)

# Create sample data for Services
services_data = [
    {"name": "Structural Analysis", "description": "In-depth structural analysis for stability and safety."},
    {"name": "Architectural Design", "description": "Creative and functional architectural design solutions."},
    {"name": "Construction Management", "description": "Effective project management from start to finish."},
    {"name": "Site Surveying", "description": "Accurate land surveying for project planning."},
    {"name": "Electrical Engineering", "description": "Electrical system design and implementation."},
    {"name": "Mechanical Engineering", "description": "Mechanical system design and optimization."},
    {"name": "Interior Design", "description": "Aesthetic interior design concepts and execution."},
    {"name": "Urban Planning", "description": "Strategic urban planning for sustainable development."},
    {"name": "Environmental Consulting", "description": "Environmental impact assessment and mitigation strategies."},
    {"name": "Project Cost Estimation", "description": "Precise project cost estimation and budgeting."},
]

for service_data in services_data:
    service = Service(**service_data)
    db.session.add(service)

# Commit the changes
db.session.commit()

print("Sample data has been successfully added to the database.")
