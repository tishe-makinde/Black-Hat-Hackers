import 'package:flutter/cupertino.dart';
import 'package:trustify_app/features/verification/presentation/widgets/number_circle.dart';

class StepRow extends StatelessWidget {
  static const double _spacing = 10.0;
  static const EdgeInsets _padding = EdgeInsets.symmetric(vertical: 8.0);
  final int index;
  final String step;
  const StepRow({
    super.key,
    required this.index,
    required this.step,
  });

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: _padding,
      child: Row(
        spacing: _spacing,
        children: [
          NumberCircle(number: index),
          Text(step),
        ],
      ),
    );
  }
}
