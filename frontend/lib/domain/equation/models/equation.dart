import 'package:freezed_annotation/freezed_annotation.dart';
import 'package:hive/hive.dart';

part 'equation.freezed.dart';
part 'equation.g.dart';

@HiveType(typeId: 0)
@freezed
class Equation with _$Equation {
  const factory Equation({
    @HiveField(0, defaultValue: '') required String equation,
  }) = _Equation;

  factory Equation.empty() => const Equation(
        equation: '',
      );
}
