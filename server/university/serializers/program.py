from rest_framework import serializers

from university.models import EducationLevel, Faculty
from university.models.program import (Program, TrainingProgram, TrainingProgramItem,
                                       ProgramTools, ProgramSkills, ProgramProfessions)

class TrainingProgramItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingProgramItem
        fields = ('name',)


class TrainingProgramSerializer(serializers.ModelSerializer):
    items = TrainingProgramItemSerializer(many=True, read_only=True)
    class Meta:
        model = TrainingProgram
        fields = ('number', 'items')


class ProgramToolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramTools
        fields = ('name', 'description','logo')


class ProgramSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramSkills
        fields = ('name',)

class ProgramProfessionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramProfessions
        fields = ('name', 'description', 'photo')


class ProgramSerializer(serializers.ModelSerializer):
    training_programs = TrainingProgramSerializer(many=True, read_only=True)
    skills = ProgramSkillsSerializer(many=True, read_only=True)
    tools = ProgramToolsSerializer(many=True, read_only=True)
    professions = ProgramProfessionsSerializer(many=True, read_only=True)
    education_level = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')

    class Meta:
        model = Program
        fields = '__all__'

class ProgramEducationLevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = EducationLevel
        fields = ('id', 'title', 'slug')

class FacultySerializer(serializers.ModelSerializer):

    class Meta:
        model = Faculty
        fields = ('id', 'title', 'slug')


class ProgramListSerializer(serializers.ModelSerializer):
    education_level = ProgramEducationLevelSerializer(many=True, read_only=True)
    faculty = FacultySerializer(many=True, read_only=True)

    class Meta:
        model = Program
        fields = ('id', 'title', 'slug', 'education_level', 'faculty')
