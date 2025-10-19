import 'package:flutter/cupertino.dart';
import 'package:trustify_app/core/theme/colors.dart';

class NumberCircle extends StatelessWidget {
  static const double _dimension = 36.0;
  static const double _fontSize = 24.0;
  static final BorderRadius _borderRadius = BorderRadius.circular(30.0);
  final int number;
  const NumberCircle({
    super.key,
    required this.number,
  });

  @override
  Widget build(BuildContext context) {
    final CupertinoThemeData theme = CupertinoTheme.of(context);
    return Container(
      width: _dimension,
      height: _dimension,
      decoration: BoxDecoration(
        color: AppColors.primary,
        borderRadius: _borderRadius,
      ),
      child: Center(
        child: Text(
          number.toString(),
          style: theme.textTheme.textStyle.copyWith(
            fontWeight: FontWeight.bold,
            fontSize: _fontSize,
            color: theme.primaryContrastingColor,
          ),
        ),
      ),
    );
  }
}
