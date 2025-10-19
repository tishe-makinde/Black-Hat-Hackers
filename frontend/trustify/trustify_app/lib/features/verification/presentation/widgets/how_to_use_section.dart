import 'package:flutter/cupertino.dart';
import 'package:trustify_app/features/verification/presentation/widgets/step_row.dart';

class HowToUseSection extends StatelessWidget {
  final List<String> steps;
  const HowToUseSection({
    super.key,
    required this.steps,
  });

  @override
  Widget build(BuildContext context) {
    final CupertinoThemeData theme = CupertinoTheme.of(context);
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          'How To Use',
          style: theme.textTheme.textStyle.copyWith(
            fontSize: 24,
            fontWeight: FontWeight.bold,
          ),
        ),
        CupertinoListSection.insetGrouped(
            dividerMargin: 0,
            additionalDividerMargin: 0,
            backgroundColor: theme.scaffoldBackgroundColor,
            margin: EdgeInsets.zero,
            children: List.generate(
              steps.length,
              (int index) => StepRow(
                index: index + 1,
                step: steps[index],
              ),
            )),
      ],
    );
  }
}
