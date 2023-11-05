// coverage:ignore-file
// GENERATED CODE - DO NOT MODIFY BY HAND
// ignore_for_file: type=lint
// ignore_for_file: unused_element, deprecated_member_use, deprecated_member_use_from_same_package, use_function_type_syntax_for_parameters, unnecessary_const, avoid_init_to_null, invalid_override_different_default_values_named, prefer_expression_function_bodies, annotate_overrides, invalid_annotation_target, unnecessary_question_mark

part of 'equation.dart';

// **************************************************************************
// FreezedGenerator
// **************************************************************************

T _$identity<T>(T value) => value;

final _privateConstructorUsedError = UnsupportedError(
    'It seems like you constructed your class using `MyClass._()`. This constructor is only meant to be used by freezed and you are not supposed to need it nor use it.\nPlease check the documentation here for more information: https://github.com/rrousselGit/freezed#custom-getters-and-methods');

/// @nodoc
mixin _$Equation {
  @HiveField(0, defaultValue: '')
  String get equation => throw _privateConstructorUsedError;

  @JsonKey(ignore: true)
  $EquationCopyWith<Equation> get copyWith =>
      throw _privateConstructorUsedError;
}

/// @nodoc
abstract class $EquationCopyWith<$Res> {
  factory $EquationCopyWith(Equation value, $Res Function(Equation) then) =
      _$EquationCopyWithImpl<$Res, Equation>;
  @useResult
  $Res call({@HiveField(0, defaultValue: '') String equation});
}

/// @nodoc
class _$EquationCopyWithImpl<$Res, $Val extends Equation>
    implements $EquationCopyWith<$Res> {
  _$EquationCopyWithImpl(this._value, this._then);

  // ignore: unused_field
  final $Val _value;
  // ignore: unused_field
  final $Res Function($Val) _then;

  @pragma('vm:prefer-inline')
  @override
  $Res call({
    Object? equation = null,
  }) {
    return _then(_value.copyWith(
      equation: null == equation
          ? _value.equation
          : equation // ignore: cast_nullable_to_non_nullable
              as String,
    ) as $Val);
  }
}

/// @nodoc
abstract class _$$EquationImplCopyWith<$Res>
    implements $EquationCopyWith<$Res> {
  factory _$$EquationImplCopyWith(
          _$EquationImpl value, $Res Function(_$EquationImpl) then) =
      __$$EquationImplCopyWithImpl<$Res>;
  @override
  @useResult
  $Res call({@HiveField(0, defaultValue: '') String equation});
}

/// @nodoc
class __$$EquationImplCopyWithImpl<$Res>
    extends _$EquationCopyWithImpl<$Res, _$EquationImpl>
    implements _$$EquationImplCopyWith<$Res> {
  __$$EquationImplCopyWithImpl(
      _$EquationImpl _value, $Res Function(_$EquationImpl) _then)
      : super(_value, _then);

  @pragma('vm:prefer-inline')
  @override
  $Res call({
    Object? equation = null,
  }) {
    return _then(_$EquationImpl(
      equation: null == equation
          ? _value.equation
          : equation // ignore: cast_nullable_to_non_nullable
              as String,
    ));
  }
}

/// @nodoc

class _$EquationImpl implements _Equation {
  const _$EquationImpl(
      {@HiveField(0, defaultValue: '') required this.equation});

  @override
  @HiveField(0, defaultValue: '')
  final String equation;

  @override
  String toString() {
    return 'Equation(equation: $equation)';
  }

  @override
  bool operator ==(dynamic other) {
    return identical(this, other) ||
        (other.runtimeType == runtimeType &&
            other is _$EquationImpl &&
            (identical(other.equation, equation) ||
                other.equation == equation));
  }

  @override
  int get hashCode => Object.hash(runtimeType, equation);

  @JsonKey(ignore: true)
  @override
  @pragma('vm:prefer-inline')
  _$$EquationImplCopyWith<_$EquationImpl> get copyWith =>
      __$$EquationImplCopyWithImpl<_$EquationImpl>(this, _$identity);
}

abstract class _Equation implements Equation {
  const factory _Equation(
          {@HiveField(0, defaultValue: '') required final String equation}) =
      _$EquationImpl;

  @override
  @HiveField(0, defaultValue: '')
  String get equation;
  @override
  @JsonKey(ignore: true)
  _$$EquationImplCopyWith<_$EquationImpl> get copyWith =>
      throw _privateConstructorUsedError;
}
