from flask import Flask, request
from flask_restful import Api, Resource
from models import db, Client, Project, TeamMember, Service

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db.init_app(app)
api = Api(app)

# Define API resources
class ClientsResource(Resource):
    def get(self):
        clients = Client.query.all()
        return [{"id": client.id, "name": client.name, "email": client.email} for client in clients]

    def post(self):
        data = request.get_json()
        new_client = Client(name=data.get('name'), email=data.get('email'))
        db.session.add(new_client)
        db.session.commit()
        return {"message": "Client created successfully", "id": new_client.id}, 201

class ClientResource(Resource):
    def get(self, client_id):
        client = Client.query.get(client_id)
        if client:
            return {"id": client.id, "name": client.name, "email": client.email}
        else:
            return {"message": "Client not found"}, 404

    def patch(self, client_id):
        data = request.get_json()
        client = Client.query.get(client_id)
        if client:
            if 'name' in data:
                client.name = data['name']
            if 'email' in data:
                client.email = data['email']
            db.session.commit()
            return {"message": "Client updated successfully"}
        else:
            return {"message": "Client not found"}, 404

    def delete(self, client_id):
        client = Client.query.get(client_id)
        if client:
            db.session.delete(client)
            db.session.commit()
            return {"message": "Client deleted successfully"}
        else:
            return {"message": "Client not found"}, 404

class ProjectsResource(Resource):
    def get(self):
        projects = Project.query.all()
        return [{"id": project.id, "title": project.title, "description": project.description} for project in projects]

    def post(self):
        data = request.get_json()
        new_project = Project(title=data.get('title'), description=data.get('description'))
        db.session.add(new_project)
        db.session.commit()
        return {"message": "Project created successfully", "id": new_project.id}, 201

class ProjectResource(Resource):
    def get(self, project_id):
        project = Project.query.get(project_id)
        if project:
            return {"id": project.id, "title": project.title, "description": project.description}
        else:
            return {"message": "Project not found"}, 404

    def patch(self, project_id):
        data = request.get_json()
        project = Project.query.get(project_id)
        if project:
            if 'title' in data:
                project.title = data['title']
            if 'description' in data:
                project.description = data['description']
            db.session.commit()
            return {"message": "Project updated successfully"}
        else:
            return {"message": "Project not found"}, 404

    def delete(self, project_id):
        project = Project.query.get(project_id)
        if project:
            db.session.delete(project)
            db.session.commit()
            return {"message": "Project deleted successfully"}
        else:
            return {"message": "Project not found"}, 404

class TeamMembersResource(Resource):
    def get(self):
        team_members = TeamMember.query.all()
        return [{"id": member.id, "name": member.name, "position": member.position} for member in team_members]

    def post(self):
        data = request.get_json()
        new_member = TeamMember(name=data.get('name'), position=data.get('position'))
        db.session.add(new_member)
        db.session.commit()
        return {"message": "Team member created successfully", "id": new_member.id}, 201

class TeamMemberResource(Resource):
    def get(self, member_id):
        member = TeamMember.query.get(member_id)
        if member:
            return {"id": member.id, "name": member.name, "position": member.position}
        else:
            return {"message": "Team member not found"}, 404

    def patch(self, member_id):
        data = request.get_json()
        member = TeamMember.query.get(member_id)
        if member:
            if 'name' in data:
                member.name = data['name']
            if 'position' in data:
                member.position = data['position']
            db.session.commit()
            return {"message": "Team member updated successfully"}
        else:
            return {"message": "Team member not found"}, 404

    def delete(self, member_id):
        member = TeamMember.query.get(member_id)
        if member:
            db.session.delete(member)
            db.session.commit()
            return {"message": "Team member deleted successfully"}
        else:
            return {"message": "Team member not found"}, 404

class ServicesResource(Resource):
    def get(self):
        services = Service.query.all()
        return [{"id": service.id, "name": service.name, "description": service.description} for service in services]

    def post(self):
        data = request.get_json()
        new_service = Service(name=data.get('name'), description=data.get('description'))
        db.session.add(new_service)
        db.session.commit()
        return {"message": "Service created successfully", "id": new_service.id}, 201

class ServiceResource(Resource):
    def get(self, service_id):
        service = Service.query.get(service_id)
        if service:
            return {"id": service.id, "name": service.name, "description": service.description}
        else:
            return {"message": "Service not found"}, 404

    def patch(self, service_id):
        data = request.get_json()
        service = Service.query.get(service_id)
        if service:
            if 'name' in data:
                service.name = data['name']
            if 'description' in data:
                service.description = data['description']
            db.session.commit()
            return {"message": "Service updated successfully"}
        else:
            return {"message": "Service not found"}, 404

    def delete(self, service_id):
        service = Service.query.get(service_id)
        if service:
            db.session.delete(service)
            db.session.commit()
            return {"message": "Service deleted successfully"}
        else:
            return {"message": "Service not found"}, 404

# Add API resource endpoints
api.add_resource(ClientsResource, '/api/clients')
api.add_resource(ClientResource, '/api/clients/<int:client_id>')
api.add_resource(ProjectsResource, '/api/projects')
api.add_resource(ProjectResource, '/api/projects/<int:project_id>')
api.add_resource(TeamMembersResource, '/api/team-members')
api.add_resource(TeamMemberResource, '/api/team-members/<int:member_id>')
api.add_resource(ServicesResource, '/api/services')
api.add_resource(ServiceResource, '/api/services/<int:service_id>')

if __name__ == '__main__':
    app.run(debug=True)

