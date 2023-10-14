import 'package:frontend/domain/equation/models/equation.dart';
import 'package:hive_flutter/adapters.dart';

const String equationBoxName = 'equations';

class DbDriver {
  Future<void> driver() async {
    await Hive.initFlutter();
    Hive.registerAdapter(EquationAdapter());
    await Hive.openBox<Equation>(equationBoxName);
  }
}
