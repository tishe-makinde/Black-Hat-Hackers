import 'package:flutter/cupertino.dart';

class VerifyButton extends StatelessWidget {
  final VoidCallback onPressed;
  const VerifyButton({
    super.key,
    required this.onPressed,
  });

  @override
  Widget build(BuildContext context) {
    final CupertinoThemeData theme = CupertinoTheme.of(context);
    return CupertinoButton.filled(
      onPressed: onPressed,
      child: Row(
        spacing: 4.0,
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Text(
            'Verify',
            style: theme.textTheme.textStyle.copyWith(
              color: theme.primaryContrastingColor,
              fontWeight: FontWeight.bold,
            ),
          ),
          Icon(CupertinoIcons.search),
        ],
      ),
    );
  }
}
