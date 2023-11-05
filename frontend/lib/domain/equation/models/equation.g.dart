// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'equation.dart';

// **************************************************************************
// TypeAdapterGenerator
// **************************************************************************

class EquationAdapter extends TypeAdapter<Equation> {
  @override
  final int typeId = 0;

  @override
  Equation read(BinaryReader reader) {
    final numOfFields = reader.readByte();
    final fields = <int, dynamic>{
      for (int i = 0; i < numOfFields; i++) reader.readByte(): reader.read(),
    };
    return Equation(
      equation: fields[0] == null ? '' : fields[0] as String,
    );
  }

  @override
  void write(BinaryWriter writer, Equation obj) {
    writer
      ..writeByte(1)
      ..writeByte(0)
      ..write(obj.equation);
  }

  @override
  int get hashCode => typeId.hashCode;

  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      other is EquationAdapter &&
          runtimeType == other.runtimeType &&
          typeId == other.typeId;
}
