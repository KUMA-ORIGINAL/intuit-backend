from rest_framework import serializers

from university.models import EducationLevel
from university.models.program import (Program, TrainingProgram, TrainingProgramItem,
                                       ProgramTools, ProgramSkills)

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


class ProgramSerializer(serializers.ModelSerializer):
    training_programs = TrainingProgramSerializer(many=True, read_only=True)
    skills = ProgramSkillsSerializer(many=True, read_only=True)
    tools = ProgramToolsSerializer(many=True, read_only=True)
    education_level = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')

    class Meta:
        model = Program
        fields = '__all__'


class ProgramListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Program
        fields = ('title', 'slug', 'education_level', 'faculty')
