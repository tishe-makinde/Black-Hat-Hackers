import 'package:flutter/cupertino.dart';

class CredibilitySemantics extends StatelessWidget {
  const CredibilitySemantics({super.key});

  @override
  Widget build(BuildContext context) {
    final CupertinoThemeData theme = CupertinoTheme.of(context);
    return Column(
      children: [
        Text(
          'Credibility',
          style: theme.textTheme.textStyle.copyWith(
            fontWeight: FontWeight.bold,
            fontSize: 28.0,
          ),
        ),
      ],
    );
  }
}
